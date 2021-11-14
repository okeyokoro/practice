//recursion
fn bouncing_ball(mut h: f64,  bounce: f64,  window: f64) -> i32 {
    if !(h > 0.0 && 0.0 < bounce && bounce < 1.0 && window < h) {
        return -1
    } 
    
    let mut count = 1;
    while bounce * h > window {
        count += 2;
        h *= bounce
    }
    count
}