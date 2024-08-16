(ns x4clojure.solutions)

; Solutions to 4clojure problems. Not all of them, skipping trivial ones

; Problem 26, Fibonacci Sequence
(defn fibo [n]
  (loop [idx n results []]
    (if (zero? idx)
      (into () results)
      (let [next-fibo (apply + (take 2 (or (seq results) '(1))))]
        (recur (dec idx) (cons next-fibo results))))))

(comment
; clever solution, assumes result starting from 0
  (def fibs (lazy-cat [0N 1N] (map + fibs (rest fibs)))))

; Problem 28, Flatten a Sequence
(defn my-flatten [coll]
    (if (sequential? coll) (mapcat my-flatten coll) [coll]))

(comment
; submitted as
  (letfn [(my-flatten [coll]
            (if (sequential? coll) (mapcat my-flatten coll) [coll]))]
    #(my-flatten %)))

; Problem 29, Get the Caps
(defn get-the-caps [text]
  (apply str (filter #(Character/isUpperCase %) text)))

(comment
; the one submitted to 4ever-clojure, for ClojureScript compatibility
  (fn [s]
    (apply str (filter #(contains? (set "ABCDEFGHIJKLMNOPQRSTUVWXYZ") %) s))))

; Problem 30, Compress a Sequence
(defn my-dedupe [xs]
  (reduce
   (fn [res curr] (if (= curr (last res)) res (conj res curr)))
   [] xs))

; Problem 32, Duplicate a Sequence
(defn duplicate-seq [xs] (mapcat #(vector % %) xs))

(comment
; clever!
  (fn [[& args]] (reduce #(conj %1 %2 %2) [] args)))

; Problem 34, Implement range
(defn my-range [x y]
  (loop [curr x res []]
    (if (= curr y)
       res
       (recur (inc curr) (conj res curr)))))

; Problem 39, Interleave Two Seq
(defn my-interleave [c1 c2] (mapcat #(vector %1 %2) c1 c2))
