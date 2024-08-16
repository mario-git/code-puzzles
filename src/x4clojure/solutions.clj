(ns x4clojure.solutions)

; Solutions to 4clojure problems. Not all of them, skipping trivial ones

(defn fibo
  "Problem 26, Fibonacci Sequence"
  [n]
  (loop [idx n results []]
    (if (zero? idx)
      (into () results)
      (let [next-fibo (apply + (take 2 (or (seq results) '(1))))]
        (recur (dec idx) (cons next-fibo results))))))

(comment
; clever solution, assumes result starting from 0
  (def fibs (lazy-cat [0N 1N] (map + fibs (rest fibs)))))

(defn my-flatten
  "Problem 28, Flatten a Sequence"
  [coll]
  (if (sequential? coll) (mapcat my-flatten coll) [coll]))

(comment
; submitted as
  (letfn [(my-flatten [coll]
            (if (sequential? coll) (mapcat my-flatten coll) [coll]))]
    #(my-flatten %)))

(defn get-the-caps
  "Problem 29, Get the Caps"
  [text]
  (apply str (filter #(Character/isUpperCase %) text)))

(comment
; the one submitted to 4ever-clojure, for ClojureScript compatibility
  (fn [s]
    (apply str (filter #(contains? (set "ABCDEFGHIJKLMNOPQRSTUVWXYZ") %) s))))

(defn my-dedupe
  "Problem 30, Compress a Sequence"
  [xs]
  (reduce
   (fn [res curr] (if (= curr (last res)) res (conj res curr)))
   [] xs))

(defn duplicate-seq
  "Problem 32, Duplicate a Sequence"
  [xs]
  (mapcat #(vector % %) xs))

(comment
; clever!
  (fn [[& args]] (reduce #(conj %1 %2 %2) [] args)))

(defn my-range
  "Problem 34, Implement range"
  [x y]
  (loop [curr x res []]
    (if (= curr y)
       res
       (recur (inc curr) (conj res curr)))))

(defn my-interleave
  "Problem 39, Interleave Two Seq"
  [c1 c2]
  (mapcat #(vector %1 %2) c1 c2))
