//! AoC day 23, 2024: LAN Party

use std::env;
use std::fs;

fn parse_input(input: &str) -> Vec<&str> {
    input.lines().collect()
}

fn part1(data: &[&str]) -> i32 {
    0
}

fn part2(data: &[&str]) -> i32 {
    0
}

fn main() {
    let input_path = env::args()
        .nth(1)
        .unwrap_or_else(|| "../input.txt".to_string());

    let input = fs::read_to_string(&input_path)
        .unwrap_or_else(|e| panic!("Failed to read input file {}: {}", input_path, e));

    let data = parse_input(&input);

    println!("Part 1: {}", part1(&data));
    println!("Part 2: {}", part2(&data));
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::path::Path;

    fn read_example() -> String {
        let example_path = Path::new("../example.txt");
        fs::read_to_string(example_path).unwrap_or_else(|e| {
            panic!(
                "Failed to read example file {}: {}",
                example_path.to_string_lossy(),
                e
            )
        })
    }

    #[test]
    fn test_part1() {
        let example = read_example();
        let data = parse_input(example);
        assert_eq!(part1(&data), 0);
    }

    #[test]
    fn test_part2() {
        let example = read_example();
        let data = parse_input(example);
        assert_eq!(part2(&data), 0);
    }
}