# Package Reuse Example

A sample project that would be used to check the name clashing.  
It consists of 2 packages, alpha and beta.  

Alpha includes multiple modules and it prints test names as a **main function**.  
Beta includes multiple modules that have name clashings with alpha, and its main function is to **print products** **call alpha** and **print products**  
Calling alpha to run its own classes instead of beta's classes is achieved by adding alpha correctly to beta's system path.

