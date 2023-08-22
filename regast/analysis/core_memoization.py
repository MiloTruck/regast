from collections import defaultdict
from typing import Dict

from regast.core.core import Core
from regast.core.declarations.source_unit import SourceUnit


def memoize_core_objects(source_unit: SourceUnit):
    # Get all core objects
    core_objects = []

    def get_core_objects(obj):
        core_objects.append(obj)
        for child in obj.children:
            get_core_objects(child)
    
    get_core_objects(source_unit)
    core_objects = list(set(core_objects))
    
    # Sort core objects according to core types
    core_type_to_instances: Dict[type, Core] = defaultdict(list)

    for core_object in core_objects:
        current_class = core_object.__class__
        while current_class != Core:
            core_type_to_instances[current_class].append(core_object)
            current_class = current_class.__bases__[0]
    
    # Add reference to core_type_to_instances to all core objects
    def add_reference_to_children(obj):
        obj._core_type_to_instances = core_type_to_instances
        for child in obj.children:
            add_reference_to_children(child)

    add_reference_to_children(source_unit)

        