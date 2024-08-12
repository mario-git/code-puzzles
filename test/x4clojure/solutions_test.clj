(ns x4clojure.solutions-test
  (:require
    [clojure.test :refer :all]
    [x4clojure.solutions :refer :all]))

(deftest problem26-fibonacci
  (is (= (solution26 3) '(1 1 2)))
  (is (= (solution26 6) '(1 1 2 3 5 8)))
  (is (= (solution26 8) '(1 1 2 3 5 8 13 21))))
