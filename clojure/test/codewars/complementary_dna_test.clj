(ns codewars.complementary-dna-test
  (:require
    [clojure.test :refer :all]
    [codewars.complementary-dna :refer [dna-strand]]))

(deftest sample-tests
  (is (= (dna-strand "ATCG") "TAGC"))
  (is (= (dna-strand "TAGC") "ATCG")))
