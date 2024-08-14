(ns x4clojure.solutions-test
  (:require
    [clojure.test :refer :all]
    [x4clojure.solutions :refer :all]))

(deftest problem26-fibonacci
  (is (= (fibo 3) '(1 1 2)))
  (is (= (fibo 6) '(1 1 2 3 5 8)))
  (is (= (fibo 8) '(1 1 2 3 5 8 13 21))))

(deftest problem28-flatten-a-sequence
  (is (= (my-flatten '((1 2) 3 [4 [5 6]])) '(1 2 3 4 5 6)))
  (is (= (my-flatten ["a" ["b"] "c"]) '("a" "b" "c")))
  (is (= (my-flatten '((((:a))))) '(:a))))

(deftest problem-29-get-the-caps
  (is (= (get-the-caps "HeLlO, WoRlD!") "HLOWRD"))
  (is (empty? (get-the-caps "nothing")))
  (is (= (get-the-caps "$#A(*&987Zf") "AZ")))
