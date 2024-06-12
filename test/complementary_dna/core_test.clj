(ns complementary-dna.core-test
  (:require
    [clojure.test :refer :all]
    [complementary-dna.core :refer [dna-strand]]))

(deftest sample-tests
  (is (= (dna-strand "ATCG") "TAGC"))
  (is (= (dna-strand "TAGC") "ATCG")))
