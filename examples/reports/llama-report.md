## Summary
### Medium Risk Issues
|&nbsp;&nbsp;&nbsp;ID&nbsp;&nbsp;&nbsp;|Issue|Instances|
|:-:|:-|:-:|
|[M-01](#m-01-use-_safemint-instead-of-_mint)|Use `_safeMint()` instead of `_mint()`|1|


Total: 1 instances over 1 issues
### Low Risk Issues
|&nbsp;&nbsp;&nbsp;ID&nbsp;&nbsp;&nbsp;|Issue|Instances|
|:-:|:-|:-:|
|[L-01](#l-01-missing-initial-value-check-in-state-variable-setter-functions)|Missing initial value check in state variable setter functions|6|
|[L-02](#l-02-safeapprove-is-deprecated)|`safeApprove()` is deprecated|1|
|[L-03](#l-03-initializers-could-be-front-run)|Initializers could be front-run|4|
|[L-04](#l-04-empty-function-body)|Empty function body|5|
|[L-05](#l-05-use-of-ecrecover-is-susceptible-to-signature-malleability)|Use of `ecrecover` is susceptible to signature malleability|3|
|[L-06](#l-06-missing-zero-address-check-for-state-variables)|Missing zero address check for state variables|1|


Total: 20 instances over 6 issues
### Non-Critical Issues
|&nbsp;&nbsp;&nbsp;ID&nbsp;&nbsp;&nbsp;|Issue|Instances|
|:-:|:-|:-:|
|[N-01](#n-01-unspecific-compiler-version-pragma)|Unspecific compiler version pragma|4|
|[N-02](#n-02-constants-in-comparisons-should-appear-on-the-left-side)|Constants in comparisons should appear on the left side|30|
|[N-03](#n-03-function-ordering-does-not-follow-the-solidity-style-guide)|Function ordering does not follow the Solidity style guide|11|
|[N-04](#n-04-unnecessary-initialization-of-variables-with-default-values)|Unnecessary initialization of variables with default values|25|
|[N-05](#n-05-inconsistent-spacing-in-comments)|Inconsistent spacing in comments|15|
|[N-06](#n-06-events-are-missing-sender-information)|Events are missing sender information|28|
|[N-07](#n-07-constants-should-be-defined-rather-than-using-magic-numbers)|Constants should be defined rather than using magic numbers|47|
|[N-08](#n-08-unused-named-return-variables)|Unused named return variables|2|
|[N-09](#n-09-constant-redefined-elsewhere)|Constant redefined elsewhere|2|
|[N-10](#n-10-public-functions-not-used-internally-can-be-declared-external)|`public` functions not used internally can be declared `external`|10|
|[N-11](#n-11-constant-variables-with-expressions-should-be-immutable-instead)|`constant` variables with expressions should be `immutable` instead|5|
|[N-12](#n-12-event-is-not-properly-indexed)|Event is not properly `indexed`|23|
|[N-13](#n-13-lines-are-too-long)|Lines are too long|22|
|[N-14](#n-14-implementation-contract-may-not-be-initialized)|Implementation contract may not be initialized|1|
|[N-15](#n-15-non-external-variable-and-function-names-should-begin-with-an-underscore)|Non-external variable and function names should begin with an underscore|15|
|[N-16](#n-16-contract-does-not-follow-the-solidity-style-guides-suggested-layout-ordering)|Contract does not follow the Solidity style guide's suggested layout ordering|10|


Total: 250 instances over 16 issues
### Gas Optimizations
|&nbsp;&nbsp;&nbsp;ID&nbsp;&nbsp;&nbsp;|Issue|Instances|Gas Saved|
|:-:|:-|:-:|:-:|
|[G-01](#g-01-internal-functions-only-called-once-can-be-inlined-to-save-gas)|`internal` functions only called once can be inlined to save gas|8|160|
|[G-02](#g-02-use-custom-errors-instead-of-require-statements)|Use custom errors instead of `require()` statements|13|-|
|[G-03](#g-03-state-variables-should-be-cached-in-stack-variables-rather-than-re-reading-them-from-storage)|State variables should be cached in stack variables rather than re-reading them from storage|15|1455|
|[G-04](#g-04-struct-variables-can-be-packed-into-fewer-storage-slots)|Struct variables can be packed into fewer storage slots|2|-|
|[G-05](#g-05-multiple-accesses-of-a-mappingarray-should-use-a-local-variable-cache)|Multiple accesses of a mapping/array should use a local variable cache|1|42|
|[G-06](#g-06-using-bool-for-storage-incurs-overhead)|Using `bool` for storage incurs overhead|14|239400|
|[G-07](#g-07-functions-guaranteed-to-revert-when-called-by-normal-users-can-be-marked-payable)|Functions guaranteed to revert when called by normal users can be marked `payable`|47|-|
|[G-08](#g-08-cache-arraylength-outside-of-for-loops)|Cache `<array>.length` outside of for-loops|9|873|
|[G-09](#g-09-use--and--instead-of-multiplicationdivision-where-possible)|Use `<<` and `>>` instead of multiplication/division where possible|1|20|
|[G-10](#g-10-use-assembly-to-check-for-address0)|Use assembly to check for `address(0)`|16|-|
|[G-11](#g-11-requirerevert-strings-longer-than-32-bytes-costs-extra-gas)|`require()`/`revert()` strings longer than 32 bytes costs extra gas|1|-|
|[G-12](#g-12-i-costs-less-gas-than-i-or-i--1)|`++i` costs less gas than `i++` or `i += 1`|4|20|
|[G-13](#g-13-constructors-can-be-marked-payable)|Constructors can be marked `payable`|10|210|
|[G-14](#g-14-use-calldata-instead-of-memory-for-function-arguments-that-do-not-get-mutated)|Use `calldata` instead of `memory` for function arguments that do not get mutated|12|3600|
|[G-15](#g-15-declare-constants-as-private-instead-of-public-to-save-gas)|Declare constants as `private` instead of `public` to save gas|3|-|
|[G-16](#g-16-x--y-costs-more-gas-than-x--x--y-for-state-variables)|`<x> += <y>` costs more gas than `<x> = <x> + <y>` for state variables|1|113|
|[G-17](#g-17-remove-or-replace-unused-state-variables)|Remove or replace unused state variables|5|-|
|[G-18](#g-18-use--0-instead-of--0-for-unsigned-integer-comparison)|Use `!= 0` instead of `> 0` for unsigned integer comparison|14|-|
|[G-19](#g-19-multiple-addressid-mappings-can-be-combined-into-a-single-mapping-of-an-addressid-to-a-struct-where-appropriate)|Multiple `address`/ID mappings can be combined into a single `mapping` of an `address`/ID to a `struct`, where appropriate|14|-|


Total: 190 instances over 19 issues with **245893 gas** saved
## Medium Risk Issues
### [M-01] Use `_safeMint()` instead of `_mint()`
`_mint()` is [discouraged](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/d4d8d2ed9798cc3383912a23b5e8d5cb602f7d4b/contracts/token/ERC721/ERC721.sol#L271) in favor of `_safeMint()` which ensures that the recipient is either an EOA or a contract that implements `IERC721Receiver`.

_Instances (**1**):_

[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L506)
```solidity
 506:     _mint(policyholder, tokenId);
```
## Low Risk Issues
### [L-01] Missing initial value check in state variable setter functions


_Instances (**6**):_

[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L183)
```solidity
 183:     llamaExecutor = _llamaExecutor;
```
[src/LlamaFactory.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaFactory.sol#L280)
```solidity
 280:     llamaPolicyMetadata = _llamaPolicyMetadata;
```
[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L233)
```solidity
 233:     name = _name;

 235:     policy = _policy;
```
[src/lib/ERC721NonTransferableMinimalProxy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/ERC721NonTransferableMinimalProxy.sol#L63)
```solidity
  63:     name = _name;

  64:     symbol = _symbol;
```
### [L-02] `safeApprove()` is deprecated
In Openzeppelin's [SafeERC20](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#SafeERC20), `safeApprove()` is deprecated in favor of `safeIncreaseAllowance()` and `safeDecreaseAllowance()`, as seen [here](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/AccessControl.sol#L204).

_Instances (**1**):_

[src/accounts/LlamaAccount.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/accounts/LlamaAccount.sol#L182)
```solidity
 182:     erc20Data.token.safeApprove(erc20Data.recipient, erc20Data.amount);
```
### [L-03] Initializers could be front-run
Initializers could be front-run, allowing an attacker to either set their own values, take ownership of the contract, and in the best case forcing a re-deployment.

_Instances (**4**):_

[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L224-L231)
```solidity
 224:   function initialize(
 225:     string memory _name,
 226:     LlamaPolicy _policy,
 227:     ILlamaStrategy _llamaStrategyLogic,
 228:     ILlamaAccount _llamaAccountLogic,
 229:     bytes[] calldata initialStrategies,
 230:     bytes[] calldata initialAccounts
 231:   ) external initializer returns (bytes32 bootstrapPermissionId) {
```
[src/strategies/LlamaRelativeQuorum.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaRelativeQuorum.sol#L156)
```solidity
 156:   function initialize(bytes memory config) external initializer {
```
[src/strategies/LlamaAbsoluteStrategyBase.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaAbsoluteStrategyBase.sol#L153)
```solidity
 153:   function initialize(bytes memory config) external virtual initializer {
```
[src/accounts/LlamaAccount.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/accounts/LlamaAccount.sol#L130)
```solidity
 130:   function initialize(bytes memory config) external initializer {
```
### [L-04] Empty function body
Functions with empty bodies should be removed or emit something. Otherwise, consider commenting why it is included.

_Instances (**5**):_

[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L359-L364)
```solidity
 359:   function transferFrom(address, /* from */ address, /* to */ uint256 /* policyId */ )
 360:     public
 361:     pure
 362:     override
 363:     nonTransferableToken
 364:   {}

 367:   function safeTransferFrom(address, /* from */ address, /* to */ uint256 /* id */ )
 368:     public
 369:     pure
 370:     override
 371:     nonTransferableToken
 372:   {}

 375:   function safeTransferFrom(address, /* from */ address, /* to */ uint256, /* policyId */ bytes calldata /* data */ )
 376:     public
 377:     pure
 378:     override
 379:     nonTransferableToken
 380:   {}

 383:   function approve(address, /* spender */ uint256 /* id */ ) public pure override nonTransferableToken {}

 386:   function setApprovalForAll(address, /* operator */ bool /* approved */ ) public pure override nonTransferableToken {}
```
### [L-05] Use of `ecrecover` is susceptible to signature malleability
`ecrecover` is susceptible to [signature malleability](https://swcregistry.io/docs/SWC-117), which could lead to signature replay attacks. Consider using OpenZeppelin's [ECDSA library](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/cryptography/ECDSA.sol#L138-L149) rather than calling `ecrecover` directly.

_Instances (**3**):_

[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L297)
```solidity
 297:     address signer = ecrecover(digest, v, r, s);

 388:     address signer = ecrecover(digest, v, r, s);

 421:     address signer = ecrecover(digest, v, r, s);
```
### [L-06] Missing zero address check for state variables


_Instances (**1**):_

[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L183)
```solidity
 183:     llamaExecutor = _llamaExecutor;
```
## Non-Critical Issues
### [N-01] Unspecific compiler version pragma
Non-library/interface files should use fixed compiler versions, not floating ones.

_Instances (**4**):_

[src/lib/ERC721NonTransferableMinimalProxy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/ERC721NonTransferableMinimalProxy.sol#L3)
```solidity
   3: pragma solidity >=0.8.0;
```
[src/llama-scripts/LlamaSingleUseScript.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/llama-scripts/LlamaSingleUseScript.sol#L2)
```solidity
   2: pragma solidity ^0.8.19;
```
[src/llama-scripts/LlamaGovernanceScript.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/llama-scripts/LlamaGovernanceScript.sol#L2)
```solidity
   2: pragma solidity ^0.8.19;
```
[src/llama-scripts/LlamaBaseScript.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/llama-scripts/LlamaBaseScript.sol#L2)
```solidity
   2: pragma solidity ^0.8.19;
```
### [N-02] Constants in comparisons should appear on the left side
Doing so will prevent [typo bugs](https://www.moserware.com/2008/01/constants-on-left-are-better-but-this.html).

_Instances (**30**):_

[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L168)
```solidity
 168:     if (numRoles == 0 || getRoleSupplyAsNumberOfHolders(ALL_HOLDERS_ROLE) == 0) revert InvalidRoleHolderInput();

 168:     if (numRoles == 0 || getRoleSupplyAsNumberOfHolders(ALL_HOLDERS_ROLE) == 0) revert InvalidRoleHolderInput();

 223:     if (balanceOf(policyholder) == 0) revert AddressDoesNotHoldPolicy(policyholder);

 426:     bool case2 = quantity == 0 && expiration == 0;

 426:     bool case2 = quantity == 0 && expiration == 0;

 453:     if (balanceOf(policyholder) == 0) _mint(policyholder);
```
[src/LlamaFactory.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaFactory.sol#L242)
```solidity
 242:     if (initialRoleHolders.length == 0) revert InvalidDeployConfiguration();
```
[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L479)
```solidity
 479:     return actionsCount == 0 ? 0 : actions[actionsCount - 1].creationTime;

 501:     if (action.minExecutionTime == 0) return ActionState.Approved;

 607:       if (quantity == 0) revert CannotCastWithZeroQuantity(policyholder, role);

 611:       if (quantity == 0) revert CannotCastWithZeroQuantity(policyholder, role);

 642:       if (i == 0) firstStrategy = strategy;
```
[src/strategies/LlamaAbsoluteQuorum.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaAbsoluteQuorum.sol#L30)
```solidity
  30:     if (approvalPolicySupply == 0) revert RoleHasZeroSupply(approvalRole);

  33:     if (disapprovalPolicySupply == 0) revert RoleHasZeroSupply(disapprovalRole);
```
[src/strategies/LlamaAbsolutePeerReview.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaAbsolutePeerReview.sol#L43)
```solidity
  43:     if (approvalPolicySupply == 0) revert RoleHasZeroSupply(approvalRole);

  46:     if (disapprovalPolicySupply == 0) revert RoleHasZeroSupply(disapprovalRole);
```
[src/strategies/LlamaRelativeQuorum.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaRelativeQuorum.sol#L179)
```solidity
 179:       if (role == 0) revert InvalidRole(0);

 187:       if (role == 0) revert InvalidRole(0);

 202:     if (approvalPolicySupply == 0) revert RoleHasZeroSupply(approvalRole);

 205:     if (disapprovalPolicySupply == 0) revert RoleHasZeroSupply(disapprovalRole);
```
[src/strategies/LlamaAbsoluteStrategyBase.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaAbsoluteStrategyBase.sol#L179)
```solidity
 179:       if (role == 0) revert InvalidRole(0);

 187:       if (role == 0) revert InvalidRole(0);
```
[src/lib/ERC721NonTransferableMinimalProxy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/ERC721NonTransferableMinimalProxy.sol#L118)
```solidity
 118:     return interfaceId == 0x01ffc9a7 // ERC165 Interface ID for ERC165

 119:       || interfaceId == 0x80ac58cd // ERC165 Interface ID for ERC721

 120:       || interfaceId == 0x5b5e139f; // ERC165 Interface ID for ERC721Metadata

 167:       to.code.length == 0

 178:       to.code.length == 0
```
[src/lib/Checkpoints.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/Checkpoints.sol#L57)
```solidity
  57:         return pos == 0 ? 0 : _unsafeAccess(self._checkpoints, pos - 1).quantity;

  85:         return pos == 0 ? 0 : _unsafeAccess(self._checkpoints, pos - 1).quantity;

 103:         if (pos == 0) {
```
### [N-03] Function ordering does not follow the Solidity style guide
According to [Solidity's style guide](https://docs.soliditylang.org/en/v0.8.17/style-guide.html#order-of-functions), functions should be laid out in the following order: `constructor()`, `receive()`, `fallback()`, `external`, `public`, `internal`, `private`. However, the contracts below do not follow this pattern.

_Instances (**11**):_

[src/LlamaPolicyMetadataParamRegistry.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicyMetadataParamRegistry.sol#L9)
```solidity
   9: contract LlamaPolicyMetadataParamRegistry {
```
[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L20)
```solidity
  20: contract LlamaPolicy is ERC721NonTransferableMinimalProxy {
```
[src/LlamaFactory.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaFactory.sol#L20)
```solidity
  20: contract LlamaFactory {
```
[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L20)
```solidity
  20: contract LlamaCore is Initializable {
```
[src/strategies/LlamaRelativeQuorum.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaRelativeQuorum.sol#L20)
```solidity
  20: contract LlamaRelativeQuorum is ILlamaStrategy, Initializable {
```
[src/strategies/LlamaAbsoluteStrategyBase.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaAbsoluteStrategyBase.sol#L22)
```solidity
  22: abstract contract LlamaAbsoluteStrategyBase is ILlamaStrategy, Initializable {
```
[src/accounts/LlamaAccount.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/accounts/LlamaAccount.sol#L20)
```solidity
  20: contract LlamaAccount is ILlamaAccount, ERC721Holder, ERC1155Holder, Initializable {
```
[src/lib/ERC721NonTransferableMinimalProxy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/ERC721NonTransferableMinimalProxy.sol#L11)
```solidity
  11: abstract contract ERC721NonTransferableMinimalProxy is Initializable {
```
[src/lib/Checkpoints.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/Checkpoints.sol#L20)
```solidity
  20: library Checkpoints {
```
[src/llama-scripts/LlamaSingleUseScript.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/llama-scripts/LlamaSingleUseScript.sol#L11)
```solidity
  11: abstract contract LlamaSingleUseScript is LlamaBaseScript {
```
[src/llama-scripts/LlamaBaseScript.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/llama-scripts/LlamaBaseScript.sol#L5)
```solidity
   5: abstract contract LlamaBaseScript {
```
### [N-04] Unnecessary initialization of variables with default values


_Instances (**25**):_

[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L105)
```solidity
 105:   uint8 public constant ALL_HOLDERS_ROLE = 0;

 151:     for (uint256 i = 0; i < roleDescriptions.length; i = LlamaUtils.uncheckedIncrement(i)) {

 155:     for (uint256 i = 0; i < roleHolders.length; i = LlamaUtils.uncheckedIncrement(i)) {

 161:     for (uint256 i = 0; i < rolePermissions.length; i = LlamaUtils.uncheckedIncrement(i)) {
```
[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L636)
```solidity
 636:     for (uint256 i = 0; i < strategyLength; i = LlamaUtils.uncheckedIncrement(i)) {

 656:     for (uint256 i = 0; i < accountLength; i = LlamaUtils.uncheckedIncrement(i)) {
```
[src/strategies/LlamaRelativeQuorum.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaRelativeQuorum.sol#L177)
```solidity
 177:     for (uint256 i = 0; i < strategyConfig.forceApprovalRoles.length; i = LlamaUtils.uncheckedIncrement(i)) {

 185:     for (uint256 i = 0; i < strategyConfig.forceDisapprovalRoles.length; i = LlamaUtils.uncheckedIncrement(i)) {
```
[src/strategies/LlamaAbsoluteStrategyBase.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaAbsoluteStrategyBase.sol#L177)
```solidity
 177:     for (uint256 i = 0; i < strategyConfig.forceApprovalRoles.length; i = LlamaUtils.uncheckedIncrement(i)) {

 185:     for (uint256 i = 0; i < strategyConfig.forceDisapprovalRoles.length; i = LlamaUtils.uncheckedIncrement(i)) {
```
[src/accounts/LlamaAccount.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/accounts/LlamaAccount.sol#L156)
```solidity
 156:     for (uint256 i = 0; i < length; i = LlamaUtils.uncheckedIncrement(i)) {

 174:     for (uint256 i = 0; i < length; i = LlamaUtils.uncheckedIncrement(i)) {

 189:     for (uint256 i = 0; i < length; i = LlamaUtils.uncheckedIncrement(i)) {

 207:     for (uint256 i = 0; i < length; i = LlamaUtils.uncheckedIncrement(i)) {

 222:     for (uint256 i = 0; i < length; i = LlamaUtils.uncheckedIncrement(i)) {

 237:     for (uint256 i = 0; i < length; i = LlamaUtils.uncheckedIncrement(i)) {

 270:     for (uint256 i = 0; i < length; i = LlamaUtils.uncheckedIncrement(i)) {

 285:     for (uint256 i = 0; i < length; i = LlamaUtils.uncheckedIncrement(i)) {
```
[src/lib/Checkpoints.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/Checkpoints.sol#L43)
```solidity
  43:         uint256 low = 0;
```
[src/llama-scripts/LlamaGovernanceScript.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/llama-scripts/LlamaGovernanceScript.sol#L71)
```solidity
  71:     for (uint256 i = 0; i < length; i = LlamaUtils.uncheckedIncrement(i)) {

 178:     for (uint256 i = 0; i < length; i = LlamaUtils.uncheckedIncrement(i)) {

 186:     for (uint256 i = 0; i < length; i = LlamaUtils.uncheckedIncrement(i)) {

 199:     for (uint256 i = 0; i < length; i = LlamaUtils.uncheckedIncrement(i)) {

 210:     for (uint256 i = 0; i < _revokePolicies.length; i = LlamaUtils.uncheckedIncrement(i)) {

 217:     for (uint256 i = 0; i < roleDescriptions.length; i = LlamaUtils.uncheckedIncrement(i)) {
```
### [N-05] Inconsistent spacing in comments
For example, some lines use `// x` and some use `//x`. The instances below point out the usages that don't follow the majority, within each file

_Instances (**15**):_

[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L400)
```solidity
 400:   //    1. An action is created that saves off the current role supply.

 401:   //    2. A policyholder is given a new role.

 402:   //    3. Now the total supply in that block is different than what it was at action creation.

 423:     //   - quantity > 0 && expiration > block.timestamp: This means you are adding a role

 424:     //   - quantity == 0 && expiration == 0: This means you are removing a role

 481:       //   1. `hadRole` and `willHaveRole` are both false.

 482:       //   2. `hadRole` and `willHaveRole` are both true, and `initialQuantity == quantity`.
```
[src/strategies/LlamaRelativeQuorum.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaRelativeQuorum.sol#L257)
```solidity
 257:     //   1. The action cannot be canceled if it's state is any of the following: Executed, Canceled,

 258:     //      Expired, Failed.

 259:     //   2. For all other states (Active, Approved, Queued) the action can be canceled if the caller

 260:     //      is the action creator.
```
[src/strategies/LlamaAbsoluteStrategyBase.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaAbsoluteStrategyBase.sol#L247)
```solidity
 247:     //   1. The action cannot be canceled if it's state is any of the following: Executed, Canceled,

 248:     //      Expired, Failed.

 249:     //   2. For all other states (Active, Approved, Queued) the action can be canceled if the caller

 250:     //      is the action creator.
```
### [N-06] Events are missing sender information
When an action is triggered based on a user's action, not being able to filter based on who triggered the action makes event processing a lot more cumbersome. Including the `msg.sender` the events of these types of action will make events much more useful to end users.

_Instances (**28**):_

[src/LlamaPolicyMetadataParamRegistry.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicyMetadataParamRegistry.sol#L84)
```solidity
  84:     emit ColorSet(llamaExecutor, _color);

  92:     emit LogoSet(llamaExecutor, _logo);
```
[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L238)
```solidity
 238:     emit RoleInitialized(role, description);

 395:     emit RoleInitialized(numRoles, description);

 486:     emit RoleAssigned(policyholder, role, expiration, quantity);

 493:     emit RolePermissionAssigned(role, permissionId, hasPermission);
```
[src/LlamaFactory.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaFactory.sol#L260-L262)
```solidity
 260:     emit LlamaInstanceCreated(
 261:       llamaCount, name, address(llamaCore), address(llamaExecutor), address(policy), block.chainid
 262:     );

 269:     emit StrategyLogicAuthorized(strategyLogic);

 275:     emit AccountLogicAuthorized(accountLogic);

 281:     emit PolicyMetadataSet(_llamaPolicyMetadata);
```
[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L357)
```solidity
 357:     emit ActionCanceled(actionInfo.id);

 447:     emit ActionGuardSet(target, selector, guard);

 457:     emit ScriptAuthorized(script, authorized);

 561:     emit ActionCreated(actionId, policyholder, role, strategy, target, value, data, description);

 572:     emit ApprovalCast(actionInfo.id, policyholder, role, quantity, reason);

 583:     emit DisapprovalCast(actionInfo.id, policyholder, role, quantity, reason);

 641:       emit StrategyCreated(strategy, llamaStrategyLogic, strategyConfigs[i]);

 660:       emit AccountCreated(account, llamaAccountLogic, accountConfigs[i]);
```
[src/strategies/LlamaRelativeQuorum.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaRelativeQuorum.sol#L182)
```solidity
 182:       emit ForceApprovalRoleAdded(role);

 190:       emit ForceDisapprovalRoleAdded(role);

 193:     emit StrategyCreated(llamaCore, policy);
```
[src/strategies/LlamaAbsoluteStrategyBase.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaAbsoluteStrategyBase.sol#L182)
```solidity
 182:       emit ForceApprovalRoleAdded(role);

 190:       emit ForceDisapprovalRoleAdded(role);

 193:     emit StrategyCreated(llamaCore, policy);
```
[src/lib/ERC721NonTransferableMinimalProxy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/ERC721NonTransferableMinimalProxy.sol#L78)
```solidity
  78:     emit Approval(owner, spender, id);

 106:     emit Transfer(from, to, id);

 139:     emit Transfer(address(0), to, id);

 156:     emit Transfer(owner, address(0), id);
```
### [N-07] Constants should be defined rather than using magic numbers
Even [assembly](https://github.com/code-423n4/2022-05-opensea-seaport/blob/9d7ce4d08bf3c3010304a0476a785c70c0e90ae7/contracts/lib/TokenTransferrer.sol#L35-L39) can benefit from using readable constants instead of hex/numeric literals

_Instances (**47**):_

[src/LlamaPolicyMetadata.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicyMetadata.sol#L22)
```solidity
/// 21
  22:     string[21] memory parts;

/// 38
  33:     parts[3] = string_concat(LibString.slice(policyholder, 0, 6), "...", LibString.slice(policyholder, 38, 42));

/// 6
  33:     parts[3] = string_concat(LibString.slice(policyholder, 0, 6), "...", LibString.slice(policyholder, 38, 42));

/// 42
  33:     parts[3] = string_concat(LibString.slice(policyholder, 0, 6), "...", LibString.slice(policyholder, 38, 42));

/// 3
  33:     parts[3] = string_concat(LibString.slice(policyholder, 0, 6), "...", LibString.slice(policyholder, 38, 42));

/// 4
  35:     parts[4] =

/// 5
  38:     parts[5] = logo;

/// 6
  40:     parts[6] =

/// 7
  43:     parts[7] = color;

/// 8
  45:     parts[8] = '" /><stop offset="1" stop-color="';

/// 9
  47:     parts[9] = color;

/// 11
  52:     parts[11] = color;

/// 12
  54:     parts[12] = '" /><stop offset="1" stop-color="';

/// 13
  56:     parts[13] = color;

/// 14
  58:     parts[14] =

/// 15
  61:     parts[15] = color;

/// 16
  63:     parts[16] = '" /><stop offset="1" stop-color="';

/// 17
  65:     parts[17] = color;

/// 18
  67:     parts[18] =

/// 19
  70:     parts[19] = color;

/// 20
  72:     parts[20] =

/// 5
  77:       string_concat(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8]);

/// 8
  77:       string_concat(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8]);

/// 3
  77:       string_concat(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8]);

/// 6
  77:       string_concat(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8]);

/// 4
  77:       string_concat(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8]);

/// 7
  77:       string_concat(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8]);

/// 13
  79:       string_concat(parts[9], parts[10], parts[11], parts[12], parts[13], parts[14], parts[15], parts[16], parts[17]);

/// 9
  79:       string_concat(parts[9], parts[10], parts[11], parts[12], parts[13], parts[14], parts[15], parts[16], parts[17]);

/// 16
  79:       string_concat(parts[9], parts[10], parts[11], parts[12], parts[13], parts[14], parts[15], parts[16], parts[17]);

/// 11
  79:       string_concat(parts[9], parts[10], parts[11], parts[12], parts[13], parts[14], parts[15], parts[16], parts[17]);

/// 14
  79:       string_concat(parts[9], parts[10], parts[11], parts[12], parts[13], parts[14], parts[15], parts[16], parts[17]);

/// 17
  79:       string_concat(parts[9], parts[10], parts[11], parts[12], parts[13], parts[14], parts[15], parts[16], parts[17]);

/// 12
  79:       string_concat(parts[9], parts[10], parts[11], parts[12], parts[13], parts[14], parts[15], parts[16], parts[17]);

/// 15
  79:       string_concat(parts[9], parts[10], parts[11], parts[12], parts[13], parts[14], parts[15], parts[16], parts[17]);

/// 18
  80:     string memory output = string_concat(output1, output2, parts[18], parts[19], parts[20]);

/// 19
  80:     string memory output = string_concat(output1, output2, parts[18], parts[19], parts[20]);

/// 20
  80:     string memory output = string_concat(output1, output2, parts[18], parts[19], parts[20]);

/// 5
 105:     string[5] memory parts;

/// 3
 109:     parts[3] = name;

/// 4
 110:     parts[4] =

/// 4
 112:     string memory json = Base64.encode(bytes(string_concat(parts[0], parts[1], parts[2], parts[3], parts[4])));

/// 3
 112:     string memory json = Base64.encode(bytes(string_concat(parts[0], parts[1], parts[2], parts[3], parts[4])));
```
[src/lib/ERC721NonTransferableMinimalProxy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/ERC721NonTransferableMinimalProxy.sol#L118)
```solidity
/// 0x01ffc9a7
 118:     return interfaceId == 0x01ffc9a7 // ERC165 Interface ID for ERC165

/// 0x80ac58cd
 119:       || interfaceId == 0x80ac58cd // ERC165 Interface ID for ERC721

/// 0x5b5e139f
 120:       || interfaceId == 0x5b5e139f; // ERC165 Interface ID for ERC721Metadata
```
[src/lib/Checkpoints.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/Checkpoints.sol#L46)
```solidity
/// 5
  46:         if (len > 5) {
```
### [N-08] Unused named return variables
Named return variables which are not used in their respective functions should be changed to an unnamed one.

_Instances (**2**):_

[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L231)
```solidity
/// bootstrapPermissionId
 231:   ) external initializer returns (bytes32 bootstrapPermissionId) {

/// timestamp
 478:   function getLastActionTimestamp() external view returns (uint256 timestamp) {
```
### [N-09] Constant redefined elsewhere
Consider defining in only one contract so that values cannot become out of sync when only one location is updated. A [cheap way](https://medium.com/coinmonks/gas-cost-of-solidity-library-functions-dbe0cedd4678) to store constants in a single location is to create an `internal constant` in a `library`. If the variable is a local cache of another contract's value, consider making the cache variable internal or private, which will require external users to query the contract with the source of truth, so that callers don't get out of sync.

_Instances (**2**):_

[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L111)
```solidity
/// Also declared in: src/LlamaFactory.sol
 111:   uint8 public constant BOOTSTRAP_ROLE = 1;
```
[src/LlamaFactory.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaFactory.sol#L68)
```solidity
/// Also declared in: src/LlamaPolicy.sol
  68:   uint8 public constant BOOTSTRAP_ROLE = 1;
```
### [N-10] `public` functions not used internally can be declared `external`
Calls to `external` functions are cheaper than `public` functions. Thus, if a function is not used internally in any contract, it should be set to `external` to save gas and improve code readability.

_Instances (**10**):_

[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L263)
```solidity
 263:   function getRoleSupplyAsQuantitySum(uint8 role) public view returns (uint128) {

 337:   function totalSupply() public view returns (uint256) {
```
[src/LlamaPolicyMetadata.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicyMetadata.sol#L104)
```solidity
 104:   function contractURI(string memory name) public pure returns (string memory) {
```
[src/strategies/LlamaRelativeQuorum.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaRelativeQuorum.sol#L288)
```solidity
 288:   function isActionDisapproved(ActionInfo calldata actionInfo) public view returns (bool) {
```
[src/strategies/LlamaAbsoluteStrategyBase.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaAbsoluteStrategyBase.sol#L278)
```solidity
 278:   function isActionDisapproved(ActionInfo calldata actionInfo) public view virtual returns (bool) {
```
[src/lib/ERC721NonTransferableMinimalProxy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/ERC721NonTransferableMinimalProxy.sol#L40)
```solidity
  40:   function ownerOf(uint256 id) public view virtual returns (address owner) {

  71:   function approve(address spender, uint256 id) public virtual {

  81:   function setApprovalForAll(address operator, bool approved) public virtual {

  87:   function transferFrom(address from, address to, uint256 id) public virtual {

 117:   function supportsInterface(bytes4 interfaceId) public view virtual returns (bool) {
```
### [N-11] `constant` variables with expressions should be `immutable` instead
While this doesn't save any gas as the compiler optimizes this, it's best practice to use `immutable` and `constant` variables where appropriate. `constant` variables should be used for literal values (eg. `1 day`) written into the code, while `immutable` variables should be used for expressions (eg. `keccak256(...)`), calculated values, or values passed into the constructor.

_Instances (**5**):_

[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L142-L143)
```solidity
 142:   bytes32 internal constant EIP712_DOMAIN_TYPEHASH =
 143:     keccak256("EIP712Domain(string name,string version,uint256 chainId,address verifyingContract)");

 146:   bytes32 internal constant CREATE_ACTION_TYPEHASH = keccak256(
 147:     "CreateAction(address policyholder,uint8 role,address strategy,address target,uint256 value,bytes data,string description,uint256 nonce)"
 148:   );

 151:   bytes32 internal constant CAST_APPROVAL_TYPEHASH = keccak256(
 152:     "CastApproval(address policyholder,uint8 role,ActionInfo actionInfo,string reason,uint256 nonce)ActionInfo(uint256 id,address creator,uint8 creatorRole,address strategy,address target,uint256 value,bytes data)"
 153:   );

 156:   bytes32 internal constant CAST_DISAPPROVAL_TYPEHASH = keccak256(
 157:     "CastDisapproval(address policyholder,uint8 role,ActionInfo actionInfo,string reason,uint256 nonce)ActionInfo(uint256 id,address creator,uint8 creatorRole,address strategy,address target,uint256 value,bytes data)"
 158:   );

 161:   bytes32 internal constant ACTION_INFO_TYPEHASH = keccak256(
 162:     "ActionInfo(uint256 id,address creator,uint8 creatorRole,address strategy,address target,uint256 value,bytes data)"
 163:   );
```
### [N-12] Event is not properly `indexed`
Index event fields make the field more quickly accessible [to off-chain tools](https://ethereum.stackexchange.com/questions/40396/can-somebody-please-explain-the-concept-of-event-indexing) that parse events. This is especially useful when it comes to filtering based on an address.

However, note that each index field costs extra gas during emission, so it's not necessarily best to index the maximum allowed per event (three fields). Where applicable, each `event` should use three `indexed` fields if there are three or more fields, and gas usage is not particularly of concern for the events in question. If there are fewer than three applicable fields, all of the applicable fields should be indexed.

_Instances (**23**):_

[src/LlamaPolicyMetadataParamRegistry.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicyMetadataParamRegistry.sol#L31)
```solidity
  31:   event ColorSet(LlamaExecutor indexed llamaExecutor, string color);

  34:   event LogoSet(LlamaExecutor indexed llamaExecutor, string logo);
```
[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L85)
```solidity
  85:   event RoleAssigned(address indexed policyholder, uint8 indexed role, uint64 expiration, uint128 quantity);

  88:   event RoleInitialized(uint8 indexed role, RoleDescription description);

  91:   event RolePermissionAssigned(uint8 indexed role, bytes32 indexed permissionId, bool hasPermission);
```
[src/LlamaFactory.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaFactory.sol#L42-L49)
```solidity
  42:   event LlamaInstanceCreated(
  43:     uint256 indexed id,
  44:     string indexed name,
  45:     address llamaCore,
  46:     address llamaExecutor,
  47:     address llamaPolicy,
  48:     uint256 chainId
  49:   );
```
[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L91-L100)
```solidity
  91:   event ActionCreated(
  92:     uint256 id,
  93:     address indexed creator,
  94:     uint8 role,
  95:     ILlamaStrategy indexed strategy,
  96:     address indexed target,
  97:     uint256 value,
  98:     bytes data,
  99:     string description
 100:   );

 103:   event ActionCanceled(uint256 id);

 106:   event ActionGuardSet(address indexed target, bytes4 indexed selector, ILlamaActionGuard actionGuard);

 109:   event ActionQueued(
 110:     uint256 id,
 111:     address indexed caller,
 112:     ILlamaStrategy indexed strategy,
 113:     address indexed creator,
 114:     uint256 minExecutionTime
 115:   );

 118:   event ActionExecuted(
 119:     uint256 id, address indexed caller, ILlamaStrategy indexed strategy, address indexed creator, bytes result
 120:   );

 123:   event ApprovalCast(uint256 id, address indexed policyholder, uint8 indexed role, uint256 quantity, string reason);

 126:   event DisapprovalCast(uint256 id, address indexed policyholder, uint8 indexed role, uint256 quantity, string reason);

 129:   event StrategyCreated(ILlamaStrategy strategy, ILlamaStrategy indexed strategyLogic, bytes initializationData);

 132:   event AccountCreated(ILlamaAccount account, ILlamaAccount indexed accountLogic, bytes initializationData);

 135:   event ScriptAuthorized(address script, bool authorized);
```
[src/strategies/LlamaRelativeQuorum.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaRelativeQuorum.sol#L75)
```solidity
  75:   event ForceApprovalRoleAdded(uint8 role);

  79:   event ForceDisapprovalRoleAdded(uint8 role);

  82:   event StrategyCreated(LlamaCore llamaCore, LlamaPolicy policy);
```
[src/strategies/LlamaAbsoluteStrategyBase.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaAbsoluteStrategyBase.sol#L83)
```solidity
  83:   event ForceApprovalRoleAdded(uint8 role);

  87:   event ForceDisapprovalRoleAdded(uint8 role);

  90:   event StrategyCreated(LlamaCore llamaCore, LlamaPolicy policy);
```
[src/lib/ERC721NonTransferableMinimalProxy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/ERC721NonTransferableMinimalProxy.sol#L20)
```solidity
  20:   event ApprovalForAll(address indexed owner, address indexed operator, bool approved);
```
### [N-13] Lines are too long
Solidity's style guide recommends a maximum line length of [120 characters](https://docs.soliditylang.org/en/v0.8.17/style-guide.html#maximum-line-length) for better readability, so lines exceeding that should be refactored into multiple lines.

_Instances (**22**):_

[src/LlamaPolicyMetadataParamRegistry.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicyMetadataParamRegistry.sol#L63)
```solidity
  63:       '<g><path fill="#fff" d="M91.749 446.038H85.15v2.785h2.54v14.483h-3.272v2.785h9.746v-2.785h-2.416v-17.268ZM104.122 446.038h-6.598v2.785h2.54v14.483h-3.271v2.785h9.745v-2.785h-2.416v-17.268ZM113.237 456.162c.138-1.435 1.118-2.2 2.885-2.2 1.767 0 2.651.765 2.651 2.423v.403l-4.859.599c-2.885.362-5.149 1.63-5.149 4.484 0 2.841 2.14 4.47 5.383 4.47 2.72 0 3.921-1.044 4.487-1.935h.276v1.685h3.782v-9.135c0-3.983-2.54-5.78-6.488-5.78-3.975 0-6.404 1.797-6.694 4.568v.418h3.726Zm-.483 5.528c0-1.1.829-1.629 2.03-1.796l3.989-.529v.626c0 2.354-1.546 3.537-3.672 3.537-1.491 0-2.347-.724-2.347-1.838ZM125.765 466.091h3.727v-9.386c0-1.796.938-2.576 2.25-2.576 1.173 0 1.753.682 1.753 1.838v10.124h3.727v-9.386c0-1.796.939-2.576 2.236-2.576 1.187 0 1.753.682 1.753 1.838v10.124h3.741v-10.639c0-2.646-1.657-4.22-4.183-4.22-2.264 0-3.312.989-3.92 2.075h-.276c-.414-.947-1.436-2.075-3.534-2.075-2.056 0-2.954.864-3.45 1.741h-.277v-1.462h-3.547v14.58ZM151.545 456.162c.138-1.435 1.118-2.2 2.885-2.2 1.767 0 2.65.765 2.65 2.423v.403l-4.859.599c-2.885.362-5.149 1.63-5.149 4.484 0 2.841 2.14 4.47 5.384 4.47 2.719 0 3.92-1.044 4.486-1.935h.276v1.685H161v-9.135c0-3.983-2.54-5.78-6.488-5.78-3.975 0-6.404 1.797-6.694 4.568v.418h3.727Zm-.484 5.528c0-1.1.829-1.629 2.03-1.796l3.989-.529v.626c0 2.354-1.546 3.537-3.672 3.537-1.491 0-2.347-.724-2.347-1.838Z"/><g fill="#6A45EC"><path d="M36.736 456.934c.004-.338.137-.661.372-.901.234-.241.552-.38.886-.389h16.748a5.961 5.961 0 0 0 2.305-.458 6.036 6.036 0 0 0 3.263-3.287c.303-.737.46-1.528.46-2.326V428h-4.738v21.573c-.004.337-.137.66-.372.901-.234.24-.552.379-.886.388H38.01a5.984 5.984 0 0 0-4.248 1.781A6.108 6.108 0 0 0 32 456.934v14.891h4.736v-14.891ZM62.868 432.111h-.21l.2.204v4.448h4.36l2.043 2.084a6.008 6.008 0 0 0-3.456 2.109 6.12 6.12 0 0 0-1.358 3.841v27.034h4.717v-27.04c.005-.341.14-.666.38-.907.237-.24.56-.378.897-.383h.726c2.783 0 3.727-1.566 4.006-2.224.28-.658.711-2.453-1.257-4.448l-4.617-4.702h-1.437M50.34 469.477a7.728 7.728 0 0 1 3.013.61c.955.403 1.82.994 2.547 1.738h5.732a12.645 12.645 0 0 0-4.634-5.201 12.467 12.467 0 0 0-6.658-1.93c-2.355 0-4.662.669-6.659 1.93a12.644 12.644 0 0 0-4.634 5.201h5.733a7.799 7.799 0 0 1 2.546-1.738 7.728 7.728 0 0 1 3.014-.61Z"/></g></g>';
```
[src/LlamaPolicyMetadata.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicyMetadata.sol#L26)
```solidity
  26:       '<svg xmlns="http://www.w3.org/2000/svg" width="390" height="500" fill="none"><g clip-path="url(#a)"><rect width="390" height="500" fill="#0B101A" rx="13.393" /><mask id="b" width="364" height="305" x="4" y="30" maskUnits="userSpaceOnUse" style="mask-type:alpha"><ellipse cx="186.475" cy="182.744" fill="#8000FF" rx="196.994" ry="131.329" transform="rotate(-31.49 186.475 182.744)" /></mask><g mask="url(#b)"><g filter="url(#c)"><ellipse cx="226.274" cy="247.516" fill="url(#d)" rx="140.048" ry="59.062" transform="rotate(-31.49 226.274 247.516)" /></g><g filter="url(#e)"><ellipse cx="231.368" cy="254.717" fill="url(#f)" rx="102.858" ry="43.378" transform="rotate(-31.49 231.368 254.717)" /></g></g><g filter="url(#g)"><ellipse cx="237.625" cy="248.969" fill="url(#h)" rx="140.048" ry="59.062" transform="rotate(-31.49 237.625 248.969)" /></g><circle cx="109.839" cy="147.893" r="22" fill="url(#i)" /><rect width="150" height="35.071" x="32" y="376.875" fill="';

  31:       '" rx="17.536" /><text xml:space="preserve" fill="#0B101A" font-family="ui-monospace,Cascadia Mono,Menlo,Monaco,Segoe UI Mono,Roboto Mono,Oxygen Mono,Ubuntu Monospace,Source Code Pro,Droid Sans Mono,Fira Mono,Courier,monospace" font-size="16"><tspan x="45.393" y="399.851">';

  36:       '</tspan></text><path fill="#fff" d="M341 127.067a11.433 11.433 0 0 0 8.066-8.067 11.436 11.436 0 0 0 8.067 8.067 11.433 11.433 0 0 0-8.067 8.066 11.43 11.43 0 0 0-8.066-8.066Z" /><path stroke="#fff" stroke-width="1.5" d="M349.036 248.018V140.875" /><circle cx="349.036" cy="259.178" r="4.018" fill="#fff" /><path stroke="#fff" stroke-width="1.5" d="M349.036 292.214v-21.429" /><path fill="#fff" d="M343.364 33.506a1.364 1.364 0 0 0-2.728 0V43.85l-7.314-7.314a1.364 1.364 0 0 0-1.929 1.928l7.315 7.315h-10.344a1.364 1.364 0 0 0 0 2.727h10.344l-7.315 7.315a1.365 1.365 0 0 0 1.929 1.928l7.314-7.314v10.344a1.364 1.364 0 0 0 2.728 0V50.435l7.314 7.314a1.364 1.364 0 0 0 1.929-1.928l-7.315-7.315h10.344a1.364 1.364 0 1 0 0-2.727h-10.344l7.315-7.315a1.365 1.365 0 0 0-1.929-1.928l-7.314 7.314V33.506ZM73.81 44.512h-4.616v1.932h1.777v10.045h-2.29v1.932h6.82V56.49h-1.69V44.512ZM82.469 44.512h-4.617v1.932h1.777v10.045h-2.29v1.932h6.82V56.49h-1.69V44.512ZM88.847 51.534c.097-.995.783-1.526 2.02-1.526 1.236 0 1.854.531 1.854 1.68v.28l-3.4.416c-2.02.251-3.603 1.13-3.603 3.11 0 1.971 1.497 3.101 3.767 3.101 1.903 0 2.743-.724 3.14-1.343h.192v1.17h2.647v-6.337c0-2.763-1.777-4.009-4.54-4.009-2.782 0-4.482 1.246-4.685 3.168v.29h2.608Zm-.338 3.835c0-.763.58-1.13 1.42-1.246l2.792-.367v.435c0 1.632-1.082 2.453-2.57 2.453-1.043 0-1.642-.502-1.642-1.275ZM97.614 58.42h2.608v-6.51c0-1.246.657-1.787 1.575-1.787.821 0 1.226.474 1.226 1.275v7.023h2.609v-6.51c0-1.247.656-1.788 1.564-1.788.831 0 1.227.474 1.227 1.275v7.023h2.618v-7.38c0-1.835-1.159-2.927-2.927-2.927-1.584 0-2.318.686-2.743 1.44h-.194c-.289-.657-1.004-1.44-2.472-1.44-1.44 0-2.067.6-2.415 1.208h-.193v-1.015h-2.483v10.114ZM115.654 51.534c.097-.995.782-1.526 2.019-1.526 1.236 0 1.854.531 1.854 1.68v.28l-3.4.416c-2.019.251-3.603 1.13-3.603 3.11 0 1.971 1.498 3.101 3.767 3.101 1.903 0 2.744-.724 3.14-1.343h.193v1.17h2.647v-6.337c0-2.763-1.778-4.009-4.54-4.009-2.782 0-4.482 1.246-4.685 3.168v.29h2.608Zm-.338 3.835c0-.763.58-1.13 1.42-1.246l2.791-.367v.435c0 1.632-1.081 2.453-2.569 2.453-1.043 0-1.642-.502-1.642-1.275ZM35.314 52.07a.906.906 0 0 1 .88-.895h11.72a4.205 4.205 0 0 0 3.896-2.597 4.22 4.22 0 0 0 .323-1.614V32h-3.316v14.964a.907.907 0 0 1-.88.894H36.205a4.206 4.206 0 0 0-2.972 1.235A4.219 4.219 0 0 0 32 52.07v10.329h3.314v-10.33ZM53.6 34.852h-.147l.141.14v3.086h3.05l1.43 1.446a4.21 4.21 0 0 0-2.418 1.463 4.222 4.222 0 0 0-.95 2.664v18.752h3.3V43.647a.909.909 0 0 1 .894-.895h.508c1.947 0 2.608-1.086 2.803-1.543.196-.456.498-1.7-.88-3.085l-3.23-3.261h-1.006" /><path fill="#fff" d="M44.834 60.77a5.448 5.448 0 0 1 3.89 1.629h4.012a8.8 8.8 0 0 0-3.243-3.608 8.781 8.781 0 0 0-12.562 3.608h4.012a5.459 5.459 0 0 1 3.89-1.629Z" />';

  41:       '</g><defs><radialGradient id="d" cx="0" cy="0" r="1" gradientTransform="rotate(-90.831 270.037 36.188) scale(115.966 274.979)" gradientUnits="userSpaceOnUse"><stop stop-color="';

  50:       '" stop-opacity="0" /></radialGradient><radialGradient id="f" cx="0" cy="0" r="1" gradientTransform="matrix(7.1866 -72.99558 127.41796 12.54463 239.305 292.746)" gradientUnits="userSpaceOnUse"><stop stop-color="';

  59:       '" stop-opacity="0" /></radialGradient><radialGradient id="h" cx="0" cy="0" r="1" gradientTransform="rotate(-94.142 264.008 51.235) scale(212.85 177.126)" gradientUnits="userSpaceOnUse"><stop stop-color="';

  68:       '" stop-opacity="0" /></radialGradient><radialGradient id="i" cx="0" cy="0" r="1" gradientTransform="matrix(23.59563 32 -33.15047 24.44394 98.506 137.893)" gradientUnits="userSpaceOnUse"><stop stop-color="#0B101A" /><stop offset=".609" stop-color="';

  73:       '" /><stop offset="1" stop-color="#fff" /></radialGradient><filter id="c" width="346.748" height="277.643" x="52.9" y="108.695" color-interpolation-filters="sRGB" filterUnits="userSpaceOnUse"><feFlood flood-opacity="0" result="BackgroundImageFix" /><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape" /><feGaussianBlur result="effect1_foregroundBlur_260_71" stdDeviation="25" /></filter><filter id="e" width="221.224" height="170.469" x="120.757" y="169.482" color-interpolation-filters="sRGB" filterUnits="userSpaceOnUse"><feFlood flood-opacity="0" result="BackgroundImageFix" /><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape" /><feGaussianBlur result="effect1_foregroundBlur_260_71" stdDeviation="10" /></filter><filter id="g" width="446.748" height="377.643" x="14.251" y="60.147" color-interpolation-filters="sRGB" filterUnits="userSpaceOnUse"><feFlood flood-opacity="0" result="BackgroundImageFix" /><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape" /><feGaussianBlur result="effect1_foregroundBlur_260_71" stdDeviation="50" /></filter><clipPath id="a"><rect width="390" height="500" fill="#fff" rx="13.393" /></clipPath></defs></svg>';

  89:           ". The owner of this NFT can participate in governance according to their roles and permissions. Visit https://app.llama.xyz/profiles/",

  91:           ' to view their profile page.", "external_url": "https://app.llama.xyz", "image": "data:image/svg+xml;base64,',

 111:       '. Visit https://app.llama.xyz to learn more.", "image":"https://llama.xyz/policy-nft/llama-profile.png", "external_link": "https://app.llama.xyz", "banner":"https://llama.xyz/policy-nft/llama-banner.png" }';
```
[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L147)
```solidity
 147:     "CreateAction(address policyholder,uint8 role,address strategy,address target,uint256 value,bytes data,string description,uint256 nonce)"

 152:     "CastApproval(address policyholder,uint8 role,ActionInfo actionInfo,string reason,uint256 nonce)ActionInfo(uint256 id,address creator,uint8 creatorRole,address strategy,address target,uint256 value,bytes data)"

 157:     "CastDisapproval(address policyholder,uint8 role,ActionInfo actionInfo,string reason,uint256 nonce)ActionInfo(uint256 id,address creator,uint8 creatorRole,address strategy,address target,uint256 value,bytes data)"
```
[src/lib/ERC721NonTransferableMinimalProxy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/ERC721NonTransferableMinimalProxy.sol#L10)
```solidity
  10: /// @author Solmate / Llama (https://github.com/transmissions11/solmate/blob/34d20fc027fe8d50da71428687024a29dc01748b/src/tokens/ERC721.sol)

  92:     require(msg.sender == from || isApprovedForAll[from][msg.sender] || msg.sender == getApproved[id], "NOT_AUTHORIZED");
```
[src/lib/Checkpoints.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/Checkpoints.sol#L18)
```solidity
  18:  * original OpenZeppelin version: https://github.com/OpenZeppelin/openzeppelin-contracts/blob/d00acef4059807535af0bd0dd0ddf619747a044b/contracts/utils/Checkpoints.sol

  67:         return _insert(self._checkpoints, LlamaUtils.toUint64(block.timestamp), LlamaUtils.toUint64(expiration), LlamaUtils.toUint128(quantity));

 119:      * @dev Pushes a (`timestamp`, `expiration`, `quantity`) pair into an ordered list of checkpoints, either by inserting a new

 220:      * @dev This was copied from Solmate v7 https://github.com/transmissions11/solmate/blob/e8f96f25d48fe702117ce76c79228ca4f20206cb/src/utils/FixedPointMathLib.sol

 221:      * @notice The math utils in solmate v7 were reviewed/audited by spearbit as part of the art gobblers audit, and are more efficient than the v6 versions.
```
### [N-14] Implementation contract may not be initialized
OpenZeppelin recommends that [implementation contracts should always be initialized](https://docs.openzeppelin.com/upgrades-plugins/1.x/writing-upgradeable#initializing_the_implementation_contract):

> Do not leave an implementation contract uninitialized. An uninitialized implementation contract can be taken over by an attacker, which may impact the proxy. To prevent the implementation contract from being used, you should invoke the `_disableInitializers` function in the constructor to automatically lock it when it is deployed.

_Instances (**1**):_

[src/lib/ERC721NonTransferableMinimalProxy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/ERC721NonTransferableMinimalProxy.sol#L11)
```solidity
  11: abstract contract ERC721NonTransferableMinimalProxy is Initializable {
```
### [N-15] Non-external variable and function names should begin with an underscore
According to the [Solidity Style Guide](https://docs.soliditylang.org/en/latest/style-guide.html#underscore-prefix-for-non-external-functions-and-variables), non-external variable and function names should begin with an underscore.

_Instances (**15**):_

[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L100)
```solidity
 100:   mapping(uint256 tokenId => mapping(uint8 role => Checkpoints.History)) internal roleBalanceCkpts;
```
[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L169)
```solidity
 169:   mapping(uint256 => Action) internal actions;
```
[src/lib/Checkpoints.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/Checkpoints.sol#L37)
```solidity
  37:     function getAtProbablyRecentTimestamp(History storage self, uint256 timestamp) internal view returns (uint128) {

  66:     function push(History storage self, uint256 quantity, uint256 expiration) internal returns (uint128, uint128) {

  76:     function push(History storage self, uint256 quantity) internal returns (uint128, uint128) {

  83:     function latest(History storage self) internal view returns (uint128) {

  92:     function latestCheckpoint(History storage self)
  93:         internal
  94:         view
  95:         returns (
  96:             bool exists,
  97:             uint64 timestamp,
  98:             uint64 expiration,
  99:             uint128 quantity
 100:         )
 101:     {

 114:     function length(History storage self) internal view returns (uint256) {

 215:     function average(uint256 a, uint256 b) private pure returns (uint256) {

 223:     function sqrt(uint256 x) internal pure returns (uint256 z) {
```
[src/lib/LlamaUtils.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/LlamaUtils.sol#L10)
```solidity
  10:   function toUint64(uint256 n) internal pure returns (uint64) {

  16:   function toUint128(uint256 n) internal pure returns (uint128) {

  22:   function uncheckedIncrement(uint256 i) internal pure returns (uint256) {
```
[src/llama-scripts/LlamaSingleUseScript.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/llama-scripts/LlamaSingleUseScript.sol#L22)
```solidity
  22:   LlamaExecutor internal immutable EXECUTOR;
```
[src/llama-scripts/LlamaBaseScript.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/llama-scripts/LlamaBaseScript.sol#L18)
```solidity
  18:   address internal immutable SELF;
```
### [N-16] Contract does not follow the Solidity style guide's suggested layout ordering
According to [Solidity's style guide](https://docs.soliditylang.org/en/v0.8.16/style-guide.html#order-of-layout), contract elements should have the following order: type declarations, state variables, events, modifiers, functions. However, the contracts below do not follow this ordering.

_Instances (**10**):_

[src/LlamaPolicyMetadataParamRegistry.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicyMetadataParamRegistry.sol#L9)
```solidity
   9: contract LlamaPolicyMetadataParamRegistry {
```
[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L20)
```solidity
  20: contract LlamaPolicy is ERC721NonTransferableMinimalProxy {
```
[src/LlamaFactory.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaFactory.sol#L20)
```solidity
  20: contract LlamaFactory {
```
[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L20)
```solidity
  20: contract LlamaCore is Initializable {
```
[src/strategies/LlamaRelativeQuorum.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaRelativeQuorum.sol#L20)
```solidity
  20: contract LlamaRelativeQuorum is ILlamaStrategy, Initializable {
```
[src/strategies/LlamaAbsoluteStrategyBase.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaAbsoluteStrategyBase.sol#L22)
```solidity
  22: abstract contract LlamaAbsoluteStrategyBase is ILlamaStrategy, Initializable {
```
[src/accounts/LlamaAccount.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/accounts/LlamaAccount.sol#L20)
```solidity
  20: contract LlamaAccount is ILlamaAccount, ERC721Holder, ERC1155Holder, Initializable {
```
[src/lib/ERC721NonTransferableMinimalProxy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/ERC721NonTransferableMinimalProxy.sol#L11)
```solidity
  11: abstract contract ERC721NonTransferableMinimalProxy is Initializable {
```
[src/llama-scripts/LlamaSingleUseScript.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/llama-scripts/LlamaSingleUseScript.sol#L11)
```solidity
  11: abstract contract LlamaSingleUseScript is LlamaBaseScript {
```
[src/llama-scripts/LlamaBaseScript.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/llama-scripts/LlamaBaseScript.sol#L5)
```solidity
   5: abstract contract LlamaBaseScript {
```
## Gas Optimizations
### [G-01] `internal` functions only called once can be inlined to save gas
Not inlining costs **20 to 40 gas** because of two extra `JUMP` instructions and additional stack operations needed for function calls.

_Instances (**8**):_

[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L404)
```solidity
 404:   function _assertNoActionCreationsAtCurrentTimestamp() internal view {

 412:   function _assertValidRoleHolderUpdate(uint8 role, uint128 quantity, uint64 expiration) internal view {

 497:   function _revokeExpiredRole(uint8 role, address policyholder) internal {
```
[src/LlamaFactory.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaFactory.sol#L285)
```solidity
 285:   function _setDeploymentMetadata(LlamaExecutor llamaExecutor, string memory color, string memory logo) internal {
```
[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L714-L722)
```solidity
 714:   function _getCreateActionTypedDataHash(
 715:     address policyholder,
 716:     uint8 role,
 717:     ILlamaStrategy strategy,
 718:     address target,
 719:     uint256 value,
 720:     bytes calldata data,
 721:     string memory description
 722:   ) internal returns (bytes32) {

 746:   function _getCastApprovalTypedDataHash(
 747:     address policyholder,
 748:     uint8 role,
 749:     ActionInfo calldata actionInfo,
 750:     string calldata reason
 751:   ) internal returns (bytes32) {

 768:   function _getCastDisapprovalTypedDataHash(
 769:     address policyholder,
 770:     uint8 role,
 771:     ActionInfo calldata actionInfo,
 772:     string calldata reason
 773:   ) internal returns (bytes32) {
```
[src/lib/ERC721NonTransferableMinimalProxy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/ERC721NonTransferableMinimalProxy.sol#L62)
```solidity
  62:   function __initializeERC721MinimalProxy (string memory _name, string memory _symbol) internal {
```
### [G-02] Use custom errors instead of `require()` statements
Instead of using error strings, to reduce deployment and runtime cost, you should use [Custom Errors](https://blog.soliditylang.org/2021/04/21/custom-errors/). This would save both deployment and runtime cost.

_Instances (**13**):_

[src/lib/ERC721NonTransferableMinimalProxy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/ERC721NonTransferableMinimalProxy.sol#L41)
```solidity
  41:     require((owner = _ownerOf[id]) != address(0), "NOT_MINTED");

  45:     require(owner != address(0), "ZERO_ADDRESS");

  74:     require(msg.sender == owner || isApprovedForAll[owner][msg.sender], "NOT_AUTHORIZED");

  88:     require(from == _ownerOf[id], "WRONG_FROM");

  90:     require(to != address(0), "INVALID_RECIPIENT");

  92:     require(msg.sender == from || isApprovedForAll[from][msg.sender] || msg.sender == getApproved[id], "NOT_AUTHORIZED");

 128:     require(to != address(0), "INVALID_RECIPIENT");

 130:     require(_ownerOf[id] == address(0), "ALREADY_MINTED");

 145:     require(owner != address(0), "NOT_MINTED");

 166:     require(
 167:       to.code.length == 0
 168:         || ERC721TokenReceiver(to).onERC721Received(msg.sender, address(0), id, "")
 169:           == ERC721TokenReceiver.onERC721Received.selector,
 170:       "UNSAFE_RECIPIENT"
 171:     );

 177:     require(
 178:       to.code.length == 0
 179:         || ERC721TokenReceiver(to).onERC721Received(msg.sender, address(0), id, data)
 180:           == ERC721TokenReceiver.onERC721Received.selector,
 181:       "UNSAFE_RECIPIENT"
 182:     );
```
[src/lib/Checkpoints.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/Checkpoints.sol#L38)
```solidity
  38:         require(timestamp < block.timestamp, "Checkpoints: timestamp is not in the past");

 135:             require(last.timestamp <= timestamp, "Checkpoint: invalid timestamp");
```
### [G-03] State variables should be cached in stack variables rather than re-reading them from storage
The instances below point to the second+ access of a state variable within a function. Caching of a state variable replaces each Gwarmaccess (100 gas) with a much cheaper stack read. Other less obvious fixes/optimizations include having local memory caches of state variable structs, or having local caches of state variable contracts/addresses.

*Saves 100 gas per instance*

_Instances (**15**):_

[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L406)
```solidity
/// llamaExecutor
 406:     address llamaCore = LlamaExecutor(llamaExecutor).LLAMA_CORE();
```
[src/LlamaFactory.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaFactory.sol#L263)
```solidity
/// llamaCount
 263:     llamaCount = LlamaUtils.uncheckedIncrement(llamaCount);
```
[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L479)
```solidity
/// actionsCount
 479:     return actionsCount == 0 ? 0 : actions[actionsCount - 1].creationTime;

/// actionsCount
 559:     actionsCount = LlamaUtils.uncheckedIncrement(actionsCount); // Safety: Can never overflow a uint256 by incrementing.

/// factory
 629:     if (address(factory).code.length > 0 && !factory.authorizedStrategyLogics(llamaStrategyLogic)) {

/// factory
 649:     if (address(factory).code.length > 0 && !factory.authorizedAccountLogics(llamaAccountLogic)) {
```
[src/strategies/LlamaRelativeQuorum.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaRelativeQuorum.sol#L193)
```solidity
/// llamaCore
 193:     emit StrategyCreated(llamaCore, policy);

/// policy
 193:     emit StrategyCreated(llamaCore, policy);

/// approvalRole
 202:     if (approvalPolicySupply == 0) revert RoleHasZeroSupply(approvalRole);

/// disapprovalRole
 205:     if (disapprovalPolicySupply == 0) revert RoleHasZeroSupply(disapprovalRole);

/// approvalRole
 216:     if (role != approvalRole && !forceApprovalRole[role]) revert InvalidRole(approvalRole);

/// disapprovalRole
 231:     if (role != disapprovalRole && !forceDisapprovalRole[role]) revert InvalidRole(disapprovalRole);
```
[src/strategies/LlamaAbsoluteStrategyBase.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaAbsoluteStrategyBase.sol#L169)
```solidity
/// policy
 169:     uint8 numRoles = policy.numRoles();

/// llamaCore
 193:     emit StrategyCreated(llamaCore, policy);

/// policy
 193:     emit StrategyCreated(llamaCore, policy);
```
### [G-04] Struct variables can be packed into fewer storage slots
With reference to the [Solidity Docs](https://docs.soliditylang.org/en/latest/internals/layout_in_storage.html):

> For each variable, a size in bytes is determined according to its type. Multiple, contiguous items that need less than 32 bytes are packed into a single storage slot if possible.

By manipulating the order of struct variables, contracts can use less storage slots which in turn saves gas.

_Instances (**2**):_

[src/strategies/LlamaAbsoluteStrategyBase.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaAbsoluteStrategyBase.sol#L27)
```solidity
/// Variable ordering with 4 slots instead of the current 5 for `Config`:
///   uint8[] forceApprovalRoles
///   uint8[] forceDisapprovalRoles
///   uint64 expirationPeriod
///   uint64 queuingPeriod
///   uint64 approvalPeriod
///   uint8 disapprovalRole
///   uint8 approvalRole
///   bool isFixedLengthApprovalPeriod
///   uint128 minDisapprovals
///   uint128 minApprovals
  27:   struct Config {
```
[src/lib/Structs.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/Structs.sol#L48)
```solidity
/// Variable ordering with 2 slots instead of the current 3 for `RolePermissionData`:
///   bytes32 permissionId
///   bool hasPermission
///   uint8 role
  48: struct RolePermissionData {
```
### [G-05] Multiple accesses of a mapping/array should use a local variable cache
The instances below point to the second+ access of a value inside a mapping/array, within a function. Caching a mapping's value in a local `storage` or `calldata` variable when the value is accessed [multiple times](https://gist.github.com/IllIllI000/ec23a57daa30a8f8ca8b9681c8ccefb0), saves **~42 gas per access** due to not having to recalculate the key's keccak256 hash (Gkeccak256 - **30 gas**) and that calculation's associated stack operations. Caching an array's struct avoids recalculating the array offsets into memory/calldata.

_Instances (**1**):_

[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L448)
```solidity
/// roleBalanceCkpts[tokenId]
 448:     roleBalanceCkpts[tokenId][role].push(willHaveRole ? quantity : 0, expiration);
```
### [G-06] Using `bool` for storage incurs overhead
Use `uint256(1)` and `uint256(2)` for true/false to avoid a Gwarmaccess (100 gas), and to avoid Gsset (20000 gas) when changing from `false` to `true`, after having been `true` in the past. See [source](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/58f635312aa21f947cae5f8578638a85aa2519f5/contracts/security/ReentrancyGuard.sol#L23-L27).

_Instances (**14**):_

[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L114)
```solidity
 114:   mapping(uint8 role => mapping(bytes32 permissionId => bool)) public canCreateAction;
```
[src/LlamaFactory.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaFactory.sol#L86)
```solidity
  86:   mapping(ILlamaStrategy => bool) public authorizedStrategyLogics;

  89:   mapping(ILlamaAccount => bool) public authorizedAccountLogics;
```
[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L189)
```solidity
 189:   mapping(uint256 => mapping(address => bool)) public approvals;

 192:   mapping(uint256 => mapping(address => bool)) public disapprovals;

 195:   mapping(ILlamaStrategy => bool) public strategies;

 198:   mapping(address => bool) public authorizedScripts;
```
[src/strategies/LlamaRelativeQuorum.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaRelativeQuorum.sol#L102)
```solidity
 102:   bool public isFixedLengthApprovalPeriod;

 130:   mapping(uint8 => bool) public forceApprovalRole;

 133:   mapping(uint8 => bool) public forceDisapprovalRole;
```
[src/strategies/LlamaAbsoluteStrategyBase.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaAbsoluteStrategyBase.sol#L107)
```solidity
 107:   bool public isFixedLengthApprovalPeriod;

 133:   mapping(uint8 => bool) public forceApprovalRole;

 136:   mapping(uint8 => bool) public forceDisapprovalRole;
```
[src/lib/ERC721NonTransferableMinimalProxy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/ERC721NonTransferableMinimalProxy.sol#L56)
```solidity
  56:   mapping(address => mapping(address => bool)) public isApprovedForAll;
```
### [G-07] Functions guaranteed to revert when called by normal users can be marked `payable`
If a function modifier such as `onlyOwner` is used, the function will revert if a normal user tries to pay the function. Marking the function as `payable` will lower the gas cost for legitimate callers because the compiler will not include checks for whether a payment was provided.

_Instances (**47**):_

[src/LlamaPolicyMetadataParamRegistry.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicyMetadataParamRegistry.sol#L82)
```solidity
  82:   function setColor(LlamaExecutor llamaExecutor, string memory _color) public onlyAuthorized(llamaExecutor) {

  90:   function setLogo(LlamaExecutor llamaExecutor, string memory _logo) public onlyAuthorized(llamaExecutor) {
```
[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L190)
```solidity
 190:   function initializeRole(RoleDescription description) external onlyLlama {

 199:   function setRoleHolder(uint8 role, address policyholder, uint128 quantity, uint64 expiration) external onlyLlama {

 207:   function setRolePermission(uint8 role, bytes32 permissionId, bool hasPermission) external onlyLlama {

 222:   function revokePolicy(address policyholder) external onlyLlama {

 236:   function updateRoleDescription(uint8 role, RoleDescription description) external onlyLlama {
```
[src/LlamaFactory.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaFactory.sol#L154-L165)
```solidity
 154:   function deploy(
 155:     string memory name,
 156:     ILlamaStrategy strategyLogic,
 157:     ILlamaAccount accountLogic,
 158:     bytes[] memory initialStrategies,
 159:     bytes[] memory initialAccounts,
 160:     RoleDescription[] memory initialRoleDescriptions,
 161:     RoleHolderData[] memory initialRoleHolders,
 162:     RolePermissionData[] memory initialRolePermissions,
 163:     string memory color,
 164:     string memory logo
 165:   ) external onlyRootLlama returns (LlamaExecutor executor, LlamaCore core) {

 183:   function authorizeStrategyLogic(ILlamaStrategy strategyLogic) external onlyRootLlama {

 190:   function authorizeAccountLogic(ILlamaAccount accountLogic) external onlyRootLlama {

 197:   function setPolicyMetadata(LlamaPolicyMetadata _llamaPolicyMetadata) external onlyRootLlama {
```
[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L429)
```solidity
 429:   function createStrategies(ILlamaStrategy llamaStrategyLogic, bytes[] calldata strategyConfigs) external onlyLlama {

 436:   function createAccounts(ILlamaAccount llamaAccountLogic, bytes[] calldata accountConfigs) external onlyLlama {

 444:   function setGuard(address target, bytes4 selector, ILlamaActionGuard guard) external onlyLlama {

 454:   function authorizeScript(address script, bool authorized) external onlyLlama {
```
[src/accounts/LlamaAccount.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/accounts/LlamaAccount.sol#L147)
```solidity
 147:   function transferNativeToken(NativeTokenData calldata nativeTokenData) public onlyLlama {

 154:   function batchTransferNativeToken(NativeTokenData[] calldata nativeTokenData) external onlyLlama {

 165:   function transferERC20(ERC20Data calldata erc20Data) public onlyLlama {

 172:   function batchTransferERC20(ERC20Data[] calldata erc20Data) external onlyLlama {

 181:   function approveERC20(ERC20Data calldata erc20Data) public onlyLlama {

 187:   function batchApproveERC20(ERC20Data[] calldata erc20Data) external onlyLlama {

 198:   function transferERC721(ERC721Data calldata erc721Data) public onlyLlama {

 205:   function batchTransferERC721(ERC721Data[] calldata erc721Data) external onlyLlama {

 214:   function approveERC721(ERC721Data calldata erc721Data) public onlyLlama {

 220:   function batchApproveERC721(ERC721Data[] calldata erc721Data) external onlyLlama {

 229:   function approveOperatorERC721(ERC721OperatorData calldata erc721OperatorData) public onlyLlama {

 235:   function batchApproveOperatorERC721(ERC721OperatorData[] calldata erc721OperatorData) external onlyLlama {

 246:   function transferERC1155(ERC1155Data calldata erc1155Data) external onlyLlama {

 255:   function batchTransferSingleERC1155(ERC1155BatchData calldata erc1155BatchData) public onlyLlama {

 268:   function batchTransferMultipleERC1155(ERC1155BatchData[] calldata erc1155BatchData) external onlyLlama {

 277:   function approveOperatorERC1155(ERC1155OperatorData calldata erc1155OperatorData) public onlyLlama {

 283:   function batchApproveOperatorERC1155(ERC1155OperatorData[] calldata erc1155OperatorData) external onlyLlama {
```
[src/llama-scripts/LlamaGovernanceScript.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/llama-scripts/LlamaGovernanceScript.sol#L62-L66)
```solidity
  62:   function aggregate(address[] calldata targets, bytes[] calldata data)
  63:     external
  64:     onlyDelegateCall
  65:     returns (bytes[] memory returnData)
  66:   {

  85:   function initializeRolesAndSetRoleHolders(
  86:     RoleDescription[] calldata description,
  87:     RoleHolderData[] calldata _setRoleHolders
  88:   ) external onlyDelegateCall {

  93:   function initializeRolesAndSetRolePermissions(
  94:     RoleDescription[] calldata description,
  95:     RolePermissionData[] calldata _setRolePermissions
  96:   ) external onlyDelegateCall {

 101:   function initializeRolesAndSetRoleHoldersAndSetRolePermissions(
 102:     RoleDescription[] calldata description,
 103:     RoleHolderData[] calldata _setRoleHolders,
 104:     RolePermissionData[] calldata _setRolePermissions
 105:   ) external onlyDelegateCall {

 111:   function createNewStrategiesAndSetRoleHolders(
 112:     CreateStrategies calldata _createStrategies,
 113:     RoleHolderData[] calldata _setRoleHolders
 114:   ) external onlyDelegateCall {

 120:   function createNewStrategiesAndInitializeRolesAndSetRoleHolders(
 121:     CreateStrategies calldata _createStrategies,
 122:     RoleDescription[] calldata description,
 123:     RoleHolderData[] calldata _setRoleHolders
 124:   ) external onlyDelegateCall {

 131:   function createNewStrategiesAndSetRolePermissions(
 132:     CreateStrategies calldata _createStrategies,
 133:     RolePermissionData[] calldata _setRolePermissions
 134:   ) external onlyDelegateCall {

 140:   function createNewStrategiesAndNewRolesAndSetRoleHoldersAndSetRolePermissions(
 141:     CreateStrategies calldata _createStrategies,
 142:     RoleDescription[] calldata description,
 143:     RoleHolderData[] calldata _setRoleHolders,
 144:     RolePermissionData[] calldata _setRolePermissions
 145:   ) external onlyDelegateCall {

 153:   function revokePoliciesAndUpdateRoleDescriptions(
 154:     address[] calldata _revokePolicies,
 155:     UpdateRoleDescription[] calldata _updateRoleDescriptions
 156:   ) external onlyDelegateCall {

 161:   function revokePoliciesAndUpdateRoleDescriptionsAndSetRoleHolders(
 162:     address[] calldata _revokePolicies,
 163:     UpdateRoleDescription[] calldata _updateRoleDescriptions,
 164:     RoleHolderData[] calldata _setRoleHolders
 165:   ) external onlyDelegateCall {

 175:   function initializeRoles(RoleDescription[] calldata description) public onlyDelegateCall {

 183:   function setRoleHolders(RoleHolderData[] calldata _setRoleHolders) public onlyDelegateCall {

 196:   function setRolePermissions(RolePermissionData[] calldata _setRolePermissions) public onlyDelegateCall {

 208:   function revokePolicies(address[] calldata _revokePolicies) public onlyDelegateCall {

 215:   function updateRoleDescriptions(UpdateRoleDescription[] calldata roleDescriptions) public onlyDelegateCall {
```
### [G-08] Cache `<array>.length` outside of for-loops
The overheads outlined below are PER LOOP, excluding the first loop:
* storage arrays incur a Gwarmaccess (**100 gas**)
* memory arrays use `MLOAD` (**3 gas**)
 * calldata arrays use `CALLDATALOAD` (**3 gas**)

Caching the length changes each of these to a `DUP<N>` (**3 gas**), and gets rid of the extra `DUP<N>` needed to store the stack offset.

_Instances (**9**):_

[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L151)
```solidity
 151:     for (uint256 i = 0; i < roleDescriptions.length; i = LlamaUtils.uncheckedIncrement(i)) {

 155:     for (uint256 i = 0; i < roleHolders.length; i = LlamaUtils.uncheckedIncrement(i)) {

 161:     for (uint256 i = 0; i < rolePermissions.length; i = LlamaUtils.uncheckedIncrement(i)) {
```
[src/strategies/LlamaRelativeQuorum.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaRelativeQuorum.sol#L177)
```solidity
 177:     for (uint256 i = 0; i < strategyConfig.forceApprovalRoles.length; i = LlamaUtils.uncheckedIncrement(i)) {

 185:     for (uint256 i = 0; i < strategyConfig.forceDisapprovalRoles.length; i = LlamaUtils.uncheckedIncrement(i)) {
```
[src/strategies/LlamaAbsoluteStrategyBase.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaAbsoluteStrategyBase.sol#L177)
```solidity
 177:     for (uint256 i = 0; i < strategyConfig.forceApprovalRoles.length; i = LlamaUtils.uncheckedIncrement(i)) {

 185:     for (uint256 i = 0; i < strategyConfig.forceDisapprovalRoles.length; i = LlamaUtils.uncheckedIncrement(i)) {
```
[src/llama-scripts/LlamaGovernanceScript.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/llama-scripts/LlamaGovernanceScript.sol#L210)
```solidity
 210:     for (uint256 i = 0; i < _revokePolicies.length; i = LlamaUtils.uncheckedIncrement(i)) {

 217:     for (uint256 i = 0; i < roleDescriptions.length; i = LlamaUtils.uncheckedIncrement(i)) {
```
### [G-09] Use `<<` and `>>` instead of multiplication/division where possible
A division/multiplication by any number `x` being a power of 2 can be calculated by shifting `log2(x)` to the right/left.

While the `MUL` and `DIV` opcodes use 5 gas, the `SHL` and `SHR` opcodes only uses 3 gas. Furthermore, Solidity's division operation also includes a division-by-0 prevention which is bypassed using shifting.

_Instances (**1**):_

[src/lib/Checkpoints.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/Checkpoints.sol#L216)
```solidity
/// (a ^ b) / 2
 216:         return (a & b) + (a ^ b) / 2; // (a + b) / 2 can overflow.
```
### [G-10] Use assembly to check for `address(0)`
*Saves 6 gas per instance*

_Instances (**16**):_

[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L181)
```solidity
 181:     if (llamaExecutor != address(0)) revert AlreadyInitialized();

 405:     if (llamaExecutor == address(0)) return; // Skip check during initialization.
```
[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L298)
```solidity
 298:     if (signer == address(0) || signer != policyholder) revert InvalidSignature();

 389:     if (signer == address(0) || signer != policyholder) revert InvalidSignature();

 422:     if (signer == address(0) || signer != policyholder) revert InvalidSignature();
```
[src/accounts/LlamaAccount.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/accounts/LlamaAccount.sol#L148)
```solidity
 148:     if (nativeTokenData.recipient == address(0)) revert ZeroAddressNotAllowed();

 166:     if (erc20Data.recipient == address(0)) revert ZeroAddressNotAllowed();

 199:     if (erc721Data.recipient == address(0)) revert ZeroAddressNotAllowed();

 247:     if (erc1155Data.recipient == address(0)) revert ZeroAddressNotAllowed();

 256:     if (erc1155BatchData.recipient == address(0)) revert ZeroAddressNotAllowed();
```
[src/lib/ERC721NonTransferableMinimalProxy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/ERC721NonTransferableMinimalProxy.sol#L41)
```solidity
  41:     require((owner = _ownerOf[id]) != address(0), "NOT_MINTED");

  45:     require(owner != address(0), "ZERO_ADDRESS");

  90:     require(to != address(0), "INVALID_RECIPIENT");

 128:     require(to != address(0), "INVALID_RECIPIENT");

 130:     require(_ownerOf[id] == address(0), "ALREADY_MINTED");

 145:     require(owner != address(0), "NOT_MINTED");
```
### [G-11] `require()`/`revert()` strings longer than 32 bytes costs extra gas


_Instances (**1**):_

[src/lib/Checkpoints.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/Checkpoints.sol#L38)
```solidity
  38:         require(timestamp < block.timestamp, "Checkpoints: timestamp is not in the past");
```
### [G-12] `++i` costs less gas than `i++` or `i += 1`
Pre-increments and pre-decrements are cheaper than post-increments and post-decrements

_Instances (**4**):_

[src/lib/ERC721NonTransferableMinimalProxy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/ERC721NonTransferableMinimalProxy.sol#L97)
```solidity
  97:       _balanceOf[from]--;

  99:       _balanceOf[to]++;

 134:       _balanceOf[to]++;

 149:       _balanceOf[owner]--;
```
### [G-13] Constructors can be marked `payable`
Payable functions cost less gas to execute, since the compiler does not have to add extra checks to ensure that a payment wasn't provided. A constructor can safely be marked as payable, since only the deployer would be able to pass funds, and the project itself would not pass any funds.

_Instances (**10**):_

[src/LlamaPolicyMetadataParamRegistry.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicyMetadataParamRegistry.sol#L57)
```solidity
  57:   constructor(LlamaExecutor rootLlamaExecutor) {
```
[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L134)
```solidity
 134:   constructor() {
```
[src/LlamaFactory.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaFactory.sol#L102-L114)
```solidity
 102:   constructor(
 103:     LlamaCore llamaCoreLogic,
 104:     ILlamaStrategy initialLlamaStrategyLogic,
 105:     ILlamaAccount initialLlamaAccountLogic,
 106:     LlamaPolicy llamaPolicyLogic,
 107:     LlamaPolicyMetadata _llamaPolicyMetadata,
 108:     string memory name,
 109:     bytes[] memory initialStrategies,
 110:     bytes[] memory initialAccounts,
 111:     RoleDescription[] memory initialRoleDescriptions,
 112:     RoleHolderData[] memory initialRoleHolders,
 113:     RolePermissionData[] memory initialRolePermissions
 114:   ) {
```
[src/LlamaExecutor.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaExecutor.sol#L15)
```solidity
  15:   constructor() {
```
[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L212)
```solidity
 212:   constructor() {
```
[src/strategies/LlamaRelativeQuorum.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaRelativeQuorum.sol#L145)
```solidity
 145:   constructor() {
```
[src/strategies/LlamaAbsoluteStrategyBase.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaAbsoluteStrategyBase.sol#L142)
```solidity
 142:   constructor() {
```
[src/accounts/LlamaAccount.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/accounts/LlamaAccount.sol#L124)
```solidity
 124:   constructor() {
```
[src/llama-scripts/LlamaSingleUseScript.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/llama-scripts/LlamaSingleUseScript.sol#L24)
```solidity
  24:   constructor(LlamaExecutor executor) {
```
[src/llama-scripts/LlamaBaseScript.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/llama-scripts/LlamaBaseScript.sol#L20)
```solidity
  20:   constructor() {
```
### [G-14] Use `calldata` instead of `memory` for function arguments that do not get mutated
Mark data types as `calldata` instead of `memory` where possible. This makes it so that the data is not automatically loaded into memory. If the data passed into the function does not need to be changed (like updating values in an array), it can be passed in as `calldata`. The one exception to this is if the argument must later be passed into another function that takes an argument that specifies `memory` storage.

_Instances (**12**):_

[src/LlamaPolicyMetadataParamRegistry.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicyMetadataParamRegistry.sol#L82)
```solidity
/// _color
  82:   function setColor(LlamaExecutor llamaExecutor, string memory _color) public onlyAuthorized(llamaExecutor) {

/// _logo
  90:   function setLogo(LlamaExecutor llamaExecutor, string memory _logo) public onlyAuthorized(llamaExecutor) {
```
[src/LlamaPolicyMetadata.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicyMetadata.sol#L17)
```solidity
/// color
  17:   function tokenURI(string memory name, uint256 tokenId, string memory color, string memory logo)

/// logo
  17:   function tokenURI(string memory name, uint256 tokenId, string memory color, string memory logo)

/// name
 104:   function contractURI(string memory name) public pure returns (string memory) {
```
[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L225)
```solidity
/// _name
 225:     string memory _name,

/// description
 523:     string memory description

/// reason
 565:   function _castApproval(address policyholder, uint8 role, ActionInfo calldata actionInfo, string memory reason)

/// reason
 576:   function _castDisapproval(address policyholder, uint8 role, ActionInfo calldata actionInfo, string memory reason)

/// description
 721:     string memory description
```
[src/lib/ERC721NonTransferableMinimalProxy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/ERC721NonTransferableMinimalProxy.sol#L62)
```solidity
/// _name
  62:   function __initializeERC721MinimalProxy (string memory _name, string memory _symbol) internal {

/// _symbol
  62:   function __initializeERC721MinimalProxy (string memory _name, string memory _symbol) internal {
```
### [G-15] Declare constants as `private` instead of `public` to save gas
If needed, the values can be read from the verified contract source code, or if there are multiple values there can be a single getter function that [returns a tuple](https://github.com/code-423n4/2022-08-frax/blob/90f55a9ce4e25bceed3a74290b854341d8de6afa/src/contracts/FraxlendPair.sol#L156-L178) of the values of all currently-public constants. Saves **3406-3606 gas** in deployment gas due to the compiler not having to create non-payable getter functions for deployment calldata, not having to store the bytes of the value outside of where it's used, and not adding another entry to the method ID table.

_Instances (**3**):_

[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L105)
```solidity
 105:   uint8 public constant ALL_HOLDERS_ROLE = 0;

 111:   uint8 public constant BOOTSTRAP_ROLE = 1;
```
[src/LlamaFactory.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaFactory.sol#L68)
```solidity
  68:   uint8 public constant BOOTSTRAP_ROLE = 1;
```
### [G-16] `<x> += <y>` costs more gas than `<x> = <x> + <y>` for state variables
Using the addition operator instead of plus-equals saves [113 gas](https://gist.github.com/IllIllI000/cbbfb267425b898e5be734d4008d4fe8)

_Instances (**1**):_

[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L394)
```solidity
 394:     numRoles += 1;
```
### [G-17] Remove or replace unused state variables
State variables that are not used in any function should be removed. If they are used in an inherited contract, they should be declared in the child contract instead.



If the state variable is overriding an interface's public function, mark the variable as `constant` or `immutable` so that it does not use a storage slot, and manually add a getter function.

For initialized variables, this would save a storage slot and reduce gas costs as follows:
* If the variable is assigned a non-zero value, saves Gsset (**20000 gas**).
* If it's assigned a zero value, saves Gsreset (**2900 gas**)

For uninitialized variables, there is no gas savings, but they should be removed to prevent confusion.

_Instances (**5**):_

[src/LlamaFactory.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaFactory.sol#L86)
```solidity
  86:   mapping(ILlamaStrategy => bool) public authorizedStrategyLogics;

  89:   mapping(ILlamaAccount => bool) public authorizedAccountLogics;
```
[src/accounts/LlamaAccount.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/accounts/LlamaAccount.sol#L118)
```solidity
 118:   string public name;
```
[src/lib/ERC721NonTransferableMinimalProxy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/ERC721NonTransferableMinimalProxy.sol#L26)
```solidity
  26:   string public name;

  28:   string public symbol;
```
### [G-18] Use `!= 0` instead of `> 0` for unsigned integer comparison


_Instances (**14**):_

[src/LlamaPolicy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicy.sol#L307)
```solidity
 307:     return quantity > 0;

 313:     return quantity > 0;

 320:     return quantity > 0 && canCreateAction[role][permissionId];

 326:     return quantity > 0 && block.timestamp > expiration;

 425:     bool case1 = quantity > 0 && expiration > block.timestamp;

 444:     bool hadRole = initialQuantity > 0;

 445:     bool willHaveRole = quantity > 0;
```
[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L629)
```solidity
 629:     if (address(factory).code.length > 0 && !factory.authorizedStrategyLogics(llamaStrategyLogic)) {

 649:     if (address(factory).code.length > 0 && !factory.authorizedAccountLogics(llamaAccountLogic)) {
```
[src/strategies/LlamaRelativeQuorum.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaRelativeQuorum.sol#L223)
```solidity
 223:     return quantity > 0 && forceApprovalRole[role] ? type(uint128).max : quantity;

 242:     return quantity > 0 && forceDisapprovalRole[role] ? type(uint128).max : quantity;
```
[src/strategies/LlamaAbsoluteStrategyBase.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaAbsoluteStrategyBase.sol#L215)
```solidity
 215:     return quantity > 0 && forceApprovalRole[role] ? type(uint128).max : quantity;

 232:     return quantity > 0 && forceDisapprovalRole[role] ? type(uint128).max : quantity;
```
[src/lib/Checkpoints.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/Checkpoints.sol#L130)
```solidity
 130:         if (pos > 0) {
```
### [G-19] Multiple `address`/ID mappings can be combined into a single `mapping` of an `address`/ID to a `struct`, where appropriate
Saves a storage slot for the mapping. Depending on the circumstances and sizes of types, can avoid a Gsset (**20000 gas**) per mapping combined. Reads and subsequent writes can also be cheaper when a function requires both values and they both fit in the same storage slot. Finally, if both fields are accessed in the same function, can save **~42 gas per access** due to [not having to recalculate the key's keccak256 hash](https://gist.github.com/IllIllI000/ec23a57daa30a8f8ca8b9681c8ccefb0) (Gkeccak256 - 30 gas) and that calculation's associated stack operations.

_Instances (**14**):_

[src/LlamaPolicyMetadataParamRegistry.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaPolicyMetadataParamRegistry.sol#L47)
```solidity
/// Group 1: color, logo
  47:   mapping(LlamaExecutor => string) public color;

/// Group 1: color, logo
  50:   mapping(LlamaExecutor => string) public logo;
```
[src/LlamaCore.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/LlamaCore.sol#L169)
```solidity
/// Group 1: actions, approvals
 169:   mapping(uint256 => Action) internal actions;

/// Group 1: actions, approvals
 189:   mapping(uint256 => mapping(address => bool)) public approvals;

/// Group 2: authorizedScripts, actionGuard
 198:   mapping(address => bool) public authorizedScripts;

/// Group 2: authorizedScripts, actionGuard
 206:   mapping(address target => mapping(bytes4 selector => ILlamaActionGuard)) public actionGuard;
```
[src/strategies/LlamaRelativeQuorum.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaRelativeQuorum.sol#L130)
```solidity
/// Group 1: forceApprovalRole, forceDisapprovalRole
 130:   mapping(uint8 => bool) public forceApprovalRole;

/// Group 1: forceApprovalRole, forceDisapprovalRole
 133:   mapping(uint8 => bool) public forceDisapprovalRole;

/// Group 2: actionApprovalSupply, actionDisapprovalSupply
 136:   mapping(uint256 => uint256) public actionApprovalSupply;

/// Group 2: actionApprovalSupply, actionDisapprovalSupply
 139:   mapping(uint256 => uint256) public actionDisapprovalSupply;
```
[src/strategies/LlamaAbsoluteStrategyBase.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/strategies/LlamaAbsoluteStrategyBase.sol#L133)
```solidity
/// Group 1: forceApprovalRole, forceDisapprovalRole
 133:   mapping(uint8 => bool) public forceApprovalRole;

/// Group 1: forceApprovalRole, forceDisapprovalRole
 136:   mapping(uint8 => bool) public forceDisapprovalRole;
```
[src/lib/ERC721NonTransferableMinimalProxy.sol](https://github.com/code-423n4/2023-06-llama/blob/main/src/lib/ERC721NonTransferableMinimalProxy.sol#L36)
```solidity
/// Group 1: _ownerOf, getApproved
  36:   mapping(uint256 => address) internal _ownerOf;

/// Group 1: _ownerOf, getApproved
  54:   mapping(uint256 => address) public getApproved;
```