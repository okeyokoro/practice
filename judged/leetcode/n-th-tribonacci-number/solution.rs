use std::collections::HashMap;

impl Solution {
    pub fn tribonacci(n: i32) -> i32 {
        let mut memotable : HashMap<i32,i32> = HashMap::new();
        
        fn dp(x:i32, memotable:&mut HashMap<i32,i32>) -> i32 {
            if x <= 1 {
                return x
            }
            
            if x == 2 {
                return 1
            }
            
            let (mut dp1, mut dp2, mut dp3) = (x-1, x-2, x-3);
            
            match memotable.get(&dp1) {
                Some(&y) => { dp1 = y }
                None => { dp1 = dp(x-1, memotable) }
            }
            
            match memotable.get(&dp2) {
                Some(&y) => { dp2 = y }
                None => { dp2 = dp(x-2, memotable) }
            }
            
            match memotable.get(&dp3) {
                Some(&y) => { dp3 = y }
                None => { dp3 = dp(x-3, memotable) }
            }
            
            memotable.insert(x, dp1 + dp2 + dp3);
            
            return dp1 + dp2 + dp3
        };
        
        return dp(n, &mut memotable)
    }
}


/*
Runtime: 0 ms, faster than 100.00% of Rust online submissions for N-th Tribonacci Number.
Memory Usage: 1.9 MB, less than 100.00% of Rust online submissions for N-th Tribonacci Number.
*/