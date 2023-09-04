// Lesson #6
fn main() {
    println!("Hello, world!");
  }
  
  fn get_nth_arg(n: usize) -> String {
    std::env::args().nth(n).unwrap()
  }
  
  #[cfg(test)]
  mod tests {
    use crate::get_nth_arg;
  
    #[test]
    fn get_nth_arg_takes_usize() {
      let _ = get_nth_arg(0usize);
      assert!(true, "Your get_nth_arg function should take a usize argument.");
    }
    #[test]
    fn get_nth_arg_returns_string() {
      let val = get_nth_arg(0);
      assert!(reg_with_con(r"target/debug/deps", val));
    }
  
    fn reg_with_con(regex: &str, file_contents: String) -> bool {
      use regex::Regex;
  
      Regex::new(regex).unwrap().is_match(&file_contents)
    }
  }
  