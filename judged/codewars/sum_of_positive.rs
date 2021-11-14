fn positive_sum(slice: &[i32]) -> i32 {
    slice
        .iter()
        .filter(|n| **n >= 0)
        .sum()

}