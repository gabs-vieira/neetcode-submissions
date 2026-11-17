impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        let mut lib = [0; 256];

        for k in s.bytes() {
            lib[k as usize] += 1;
        }

        for k in t.bytes() {
            if lib[k as usize] == 0 {
                return false;
            }

            lib[k as usize] -= 1;
        }

        for i in lib {
            if i != 0 {
                return false;
            }
        }

        true
    }
}