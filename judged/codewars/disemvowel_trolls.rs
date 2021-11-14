fn disemvowel(s: &str) -> String {
    let mut ans = String::new();
    let vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
    for c in s.chars() {
        if !vowels.contains(&c) {
            ans.push(c)
        }
    }
    return ans
}