fn longest(a1: &str, a2: &str) -> String {
    ('a'..='z')
        .filter( |c| (a1.contains(*c) || a2.contains(*c)) )
        .collect()
}
