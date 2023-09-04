// Lesson #15
fn main() {
    let args = Args::new();
    println!("Hello, world!");
}

#[derive(Debug)]
struct Args {
    image_1: String,
}

impl Args {
    fn new() -> Self {
        Args {
            image_1: String::new(),
        }
    }
}

fn get_nth_arg(n: usize) -> String {
    std::env::args().nth(n).unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    #[should_panic]
    fn args_struct_has_image_1_field() {
        let new_arg = Args::new();
        let my_arg = Args {
            image_1: get_nth_arg(1),
        };
        assert!(new_arg.image_1 == my_arg.image_1);
    }

    #[test]
    fn image_1_defined_with_args() {
        let file_contents = return_file_in_src("main.rs");
        assert!(reg_with_con(r"image_1:\s*get_nth_arg\(1\)", file_contents));
    }

    fn reg_with_con(regex: &str, file_contents: String) -> bool {
        use regex::Regex;

        Regex::new(regex).unwrap().is_match(&file_contents)
    }
    fn return_file_in_src(filename: &str) -> String {
        use std::fs::read_to_string;

        match read_to_string(String::from("combiner/src/") + filename) {
            Ok(file_contents) => file_contents,
            Err(_) => String::from(""),
        }
    }
}
