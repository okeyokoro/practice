

fn printer_error(s: &str) -> String {
    let good = 'a'..='m';
    let mut count = 0;
    for c in s.chars() {
        if !good.contains(&c) {
            count += 1
        }
    }
    format!("{}/{}", count, s.len())
}

/*
fn printer_error(s: &str) -> String {
    format!("{}/{}",
        s.chars().filter(|c| !('a'..='m').contains(&c)).count(),
        s.len())
}
*/


