(ns codewars.vector-affinity-test
  (:require [clojure.test :refer :all]
            [codewars.vector-affinity :refer :all]))

(deftest SampleTests
  (is (= (vector-affinity [1 2 3 4] [1 2 3 5]) 0.75))
  (is (= (vector-affinity [] [1 2 3 4 5]) 0.0))
  (is (= (vector-affinity [6 6 6 6 6 6] [6 nil nil 6 6 nil]) (float (/ 3 6))))
  (is (= (vector-affinity [6 6 6 6 6 6] [6]) (float (/ 1 6))))
  (is (= (vector-affinity [] []) 1.0)))
