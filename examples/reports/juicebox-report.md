## Summary

### Medium Risk Issues
|Label|Issue|Instances|
|:-|:-|:-:|
|M-01|Unsafe `transfer()` for ERC20 tokens|2|

Total: 2 instances over 1 issue
### Low Risk Issues
|Label|Issue|Instances|
|:-|:-|:-:|
|L-01|Empty function body|1|

Total: 1 instances over 1 issue
### Non-Critical Issues
|Label|Issue|Instances|
|:-|:-|:-:|
|N-01|Lines are too long|4|
|N-02|Inconsistent spacing in comments|16|
|N-03|Function ordering does not follow the Solidity style guide|1|
|N-04|Redundant `return` statements|1|
|N-05|`constants` should be defined rather than using magic numbers|1|
|N-06|Event is not properly `indexed`|2|
|N-07|Unused `override` function arguments|1|
|N-08|Use scientific notation (e.g. `1e18`) rather than exponentiation (e.g. `10**18`)|1|
|N-09|Unused named return variables|2|
|N-10|Import declarations should import specific identifiers, rather than the whole file|17|


Total: 46 instances over 10 issues
### Gas Optimizations
|Label|Issue|Instances|
|:-|:-|:-:|
|G-01|Constructors can be marked `payable`|1|
|G-02|Using `bool` for storage incurs overhead|1|
|G-03|`internal` functions only called once can be inlined to save gas|1|
|G-04|`abi.encode()` is less gas efficient than `abi.encodepacked()`|1|

Total: 4 instances over 4 issues
## Medium Risk Issues
### Unsafe `transfer()` for ERC20 tokens
Using `transfer()` for ERC20 tokens without checking its return value could be dangerous for no-revert-on-failure tokens. Consider using `safeTransfer()` from Openzeppelin's [SafeERC20](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#SafeERC20) library instead.

_Instances (**2**):_
```solidity
juice-buyback/contracts/JBXBuybackDelegate.sol:
 232:         weth.transfer(address(pool), _amountToSend);
 286:         if (_nonReservedToken != 0) projectToken.transfer(_data.beneficiary, _nonReservedToken);
```

## Low Risk Issues
### [L-01] Empty function body
Functions with empty bodies should be removed or emit something. Otherwise, consider commenting why it is included.

_Instances (**1**):_
```solidity
juice-buyback/contracts/JBXBuybackDelegate.sol:
 235:     function redeemParams(JBRedeemParamsData calldata _data)
 236:         external
 237:         override
 238:         returns (uint256 reclaimAmount, string memory memo, JBRedemptionDelegateAllocation[] memory delegateAllocations)
 239:     {}
```
## Non-Critical Issues
### [N-01] Lines are too long
Solidity's style guide recommends a maximum line length of [120 characters](https://docs.soliditylang.org/en/v0.8.17/style-guide.html#maximum-line-length) for better readability, so lines exceeding that should be refactored into multiple lines.

_Instances (**4**):_
```solidity
juice-buyback/contracts/JBXBuybackDelegate.sol:
 138:      * @param  _data the data passed to the data source in terminal.pay(..). _data.metadata need to have the Uniswap quote

 179:      *         If the beneficiary requests non claimed token, the swap is not used (as it is, per definition, claimed token)

 301:             // 2) Mint the reserved token with this address as beneficiary -> result: _amountReceived-reserved here, reservedToken in reserve

 311:             // 3) Burn the non-reserve token which are now left in this address (can be 0) -> result: 0 here, reservedToken in reserve
```
### [N-02] Inconsistent spacing in comments
For example, some lines use `// x` and some use `//x`. The instances below point out the usages that don't follow the majority, within each file

_Instances (**16**):_
```solidity
juice-buyback/contracts/JBXBuybackDelegate.sol:
  42:     //*********************************************************************//

  44:     //*********************************************************************//

  49:     //*********************************************************************//

  51:     //*********************************************************************//

  56:     //*********************************************************************//

  58:     //*********************************************************************//

  70:     //*********************************************************************//

  72:     //*********************************************************************//

  97:     //*********************************************************************//

  99:     //*********************************************************************//

 131:     //*********************************************************************//

 133:     //*********************************************************************//

 241:     //*********************************************************************//

 243:     //*********************************************************************//

 355:     //*********************************************************************//

 357:     //*********************************************************************//
```
### [N-03] Function ordering does not follow the Solidity style guide
According to the [Solidity style guide](https://docs.soliditylang.org/en/v0.8.17/style-guide.html#order-of-functions), functions should be laid out in the following order: `constructor()`, `receive()`, `fallback()`, `external`, `public`, `internal`, `private`. However, the contracts below do not follow this pattern.

_Instances (**1**):_
```solidity
juice-buyback/contracts/JBXBuybackDelegate.sol:
  39: contract JBXBuybackDelegate is IJBFundingCycleDataSource, IJBPayDelegate, IUniswapV3SwapCallback, Ownable {
```
### [N-04] Redundant `return` statements
Adding a `return` statement when the function defines a named return variable, is redundant and can be removed.

_Instances (**1**):_
```solidity
juice-buyback/contracts/JBXBuybackDelegate.sol:
 274:             return _amountReceived;
```
### [N-05] `constants` should be defined rather than using magic numbers
Even [assembly](https://github.com/code-423n4/2022-05-opensea-seaport/blob/9d7ce4d08bf3c3010304a0476a785c70c0e90ae7/contracts/lib/TokenTransferrer.sol#L35-L39) can benefit from using readable constants instead of hex/numeric literals

_Instances (**1**):_
```solidity
juice-buyback/contracts/JBXBuybackDelegate.sol:
/// 18
 150:         uint256 _tokenCount = PRBMath.mulDiv(_data.amount.value, _data.weight, 10 ** 18);
```
### [N-06] Event is not properly `indexed`
Index event fields make the field more quickly accessible [to off-chain tools](https://ethereum.stackexchange.com/questions/40396/can-somebody-please-explain-the-concept-of-event-indexing) that parse events. This is especially useful when it comes to filtering based on an address.

However, note that each index field costs extra gas during emission, so it's not necessarily best to index the maximum allowed per event (three fields). Where applicable, each `event` should use three `indexed` fields if there are three or more fields, and gas usage is not particularly of concern for the events in question. If there are fewer than three applicable fields, all of the applicable fields should be indexed.

_Instances (**2**):_
```solidity
juice-buyback/contracts/JBXBuybackDelegate.sol:
  53:     event JBXBuybackDelegate_Swap(uint256 projectId, uint256 amountEth, uint256 amountOut);

  54:     event JBXBuybackDelegate_Mint(uint256 projectId);
```
### [N-07] Unused `override` function arguments
For functions declared as `override`, unused arguments should have the variable name removed or commented out to avoid compiler warnings.

_Instances (**1**):_
```solidity
juice-buyback/contracts/JBXBuybackDelegate.sol:
/// _data
 235:     function redeemParams(JBRedeemParamsData calldata _data)
```
### [N-08] Use scientific notation (e.g. `1e18`) rather than exponentiation (e.g. `10**18`)
While the compiler knows to optimize away the exponentiation, it's still better coding practice to use idioms that do not require compiler optimization, if they exist.

_Instances (**1**):_
```solidity
juice-buyback/contracts/JBXBuybackDelegate.sol:
/// 10 ** 18
 150:         uint256 _tokenCount = PRBMath.mulDiv(_data.amount.value, _data.weight, 10 ** 18);
```

### [N-09] Unused named return variables
Named return variables which are not used in their respective functinosn should be changed to an unnamed one.

_Instances (**2**):_
```solidity
juice-buyback/contracts/JBXBuybackDelegate.sol:
/// weight, memo
 147:         returns (uint256 weight, string memory memo, JBPayDelegateAllocation[] memory delegateAllocations)

 238:         returns (uint256 reclaimAmount, string memory memo, JBRedemptionDelegateAllocation[] memory delegateAllocations)
```

### [N-10] Import declarations should import specific identifiers, rather than the whole file
Solidity's documentation [recommends](https://docs.soliditylang.org/en/v0.8.15/layout-of-source-files.html#importing-other-source-files) specifying imported symbols explicitly to avoid polluting the symbol namespace. This can be done through import declarations of the form `import {<identifier_name>} from "some/file.sol"`.

_Instances (**17**):_
```solidity
juice-buyback/contracts/JBXBuybackDelegate.sol:
   4: import "@jbx-protocol/juice-contracts-v3/contracts/interfaces/IJBController3_1.sol";

   5: import "@jbx-protocol/juice-contracts-v3/contracts/interfaces/IJBFundingCycleDataSource.sol";

   6: import "@jbx-protocol/juice-contracts-v3/contracts/interfaces/IJBPayDelegate.sol";

   7: import "@jbx-protocol/juice-contracts-v3/contracts/interfaces/IJBPayoutRedemptionPaymentTerminal3_1.sol";

   8: import "@jbx-protocol/juice-contracts-v3/contracts/interfaces/IJBFundingCycleBallot.sol";

   9: import "@jbx-protocol/juice-contracts-v3/contracts/libraries/JBConstants.sol";

  10: import "@jbx-protocol/juice-contracts-v3/contracts/libraries/JBFundingCycleMetadataResolver.sol";

  11: import "@jbx-protocol/juice-contracts-v3/contracts/libraries/JBTokens.sol";

  12: import "@jbx-protocol/juice-contracts-v3/contracts/structs/JBDidPayData.sol";

  13: import "@jbx-protocol/juice-contracts-v3/contracts/structs/JBPayParamsData.sol";

  15: import "@openzeppelin/contracts/access/Ownable.sol";

  16: import "@openzeppelin/contracts/interfaces/IERC20.sol";

  18: import "@paulrberg/contracts/math/PRBMath.sol";

  20: import "@uniswap/v3-core/contracts/interfaces/IUniswapV3Pool.sol";

  21: import "@uniswap/v3-core/contracts/interfaces/callback/IUniswapV3SwapCallback.sol";

  22: import "@uniswap/v3-core/contracts/libraries/TickMath.sol";

  24: import "./interfaces/external/IWETH9.sol";
```

## Gas Optimizations
### [G-01] Constructors can be marked `payable`
Payable functions cost less gas to execute, since the compiler does not have to add extra checks to ensure that a payment wasn't provided. A constructor can safely be marked as payable, since only the deployer would be able to pass funds, and the project itself would not pass any funds.

_Instances (**1**):_
```solidity
juice-buyback/contracts/JBXBuybackDelegate.sol:
 118:     constructor(
 119:         IERC20 _projectToken,
 120:         IWETH9 _weth,
 121:         IUniswapV3Pool _pool,
 122:         IJBPayoutRedemptionPaymentTerminal3_1 _jbxTerminal
 123:     ) {
```
### [G-02] Using `bool` for storage incurs overhead
Use `uint256(1)` and `uint256(2)` for true/false to avoid a Gwarmaccess (100 gas), and to avoid Gsset (20000 gas) when changing from ‘false’ to ‘true’, after having been ‘true’ in the past. See [source](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/58f635312aa21f947cae5f8578638a85aa2519f5/contracts/security/ReentrancyGuard.sol#L23-L27).

_Instances (**1**):_
```solidity
juice-buyback/contracts/JBXBuybackDelegate.sol:
  63:     bool private immutable _projectTokenIsZero;
```
### [G-03] `internal` functions only called once can be inlined to save gas
Not inlining costs **20 to 40 gas** because of two extra `JUMP` instructions and additional stack operations needed for function calls.

_Instances (**1**):_
```solidity
juice-buyback/contracts/JBXBuybackDelegate.sol:
 258:     function _swap(JBDidPayData calldata _data, uint256 _minimumReceivedFromSwap, uint256 _reservedRate)
 259:         internal
 260:         returns (uint256 _amountReceived)
 261:     {
```

### [G-04] `abi.encode()` is less gas efficient than `abi.encodepacked()`
For variables with fixed sizes, consider using `abi.encodePacked()` instead of `abi.encode()`.

_Instances (**1**):_
```solidity
juice-buyback/contracts/JBXBuybackDelegate.sol:
 268:             data: abi.encode(_minimumReceivedFromSwap)
```