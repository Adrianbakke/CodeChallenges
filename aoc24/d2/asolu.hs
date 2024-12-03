import System.IO
import Control.Monad (forM_)
import Data.List (tails)

-- Function to calculate differences between consecutive elements
diff_ :: [Int] -> [Int]
diff_ xs = zipWith (-) xs (tail xs)

-- Function to test the sequence
test_ :: [Int] -> Bool
test_ seq = all (/= 0) seq && all (\e -> abs e < 4) seq && all (\c -> signum (seq !! (c - 1)) == signum (seq !! c)) [1..length seq - 1]

-- Function to check a sequence against the conditions
checkSequence :: [Int] -> Bool
checkSequence xs = test_ (diff_ xs) || any (test_ . diff_) (init $ tails xs)

main :: IO ()
main = do
    -- Read input from file
    contents <- readFile "input.txt"
    let xss = map (map read . words) (lines contents) :: [[Int]]

    -- Calculate the result
    let res = length $ filter id $ map checkSequence xss

    -- Print the result
    print res

