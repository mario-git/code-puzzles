(ns dir-reduc.core-test
  (:require [clojure.test :refer :all]
            [dir-reduc.core :refer :all]))

(deftest dir-reduc-test
  (testing "Reduce to single value"
    (let [ur ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
          vr ["WEST"]]
         (is (= (dirReduc ur) vr))))
  (testing "Not reducible"
    (let [not-reducible ["NORTH", "WEST", "SOUTH", "EAST"]]
      (is (= (dirReduc not-reducible) not-reducible))))
  (testing "Array fully reducible"
    (let [fully-reducible ["NORTH" "SOUTH" "SOUTH" "EAST" "WEST" "NORTH"]]
      (is (= (dirReduc fully-reducible) nil))))
  (testing "Empty array case"
    (is (= (dirReduc []) nil))))
