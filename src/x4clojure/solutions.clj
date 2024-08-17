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

(defn my-interpose
  "Problem 40, Interpose a Seq"
  [x coll]
  (loop [left (next coll) result [(first coll)]]
    (if (nil? left)
      result
      (recur (next left) (conj result x (first left))))))

(defn drop-every-nth
  "Problem 41, Drop Every Nth Item"
  [coll n]
  (filter some? (map #(when (pos? (mod (inc %1) n)) %2) (range) coll)))

(comment
; nice ones
  (fn [coll x] (keep-indexed #(when (not (zero? (mod (inc %1) x))) %2) coll))
  (fn [s c] (mapcat #(take (dec c) %) (partition-all c s))))

(defn factorial-fun
  "Problem 42, Factorial Fun"
  [n]
  (reduce * (range 1 (inc n))))
