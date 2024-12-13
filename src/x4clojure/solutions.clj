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
  (rest (reduce #(conj %1 x %2) [] coll)))

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

(defn reverse-interleave
  "Problem 43, Reverse Interleave"
  [coll n]
  (apply map list (partition n coll)))

(comment
; nice one
  (fn [s n] (for [i (range n)] (take-nth n (drop i s)))))

(defn rotate-seq
  "Problem 44, Rotate Sequence"
  [n coll]
  (let [length (count coll)
        mod-n (mod n length)
        steps (if (pos? mod-n) mod-n (+ length mod-n))]
    (->> (cycle coll)
         (drop steps)
         (take length))))

(comment
; nice ones
  #(let[n (mod %1 (count %2))] (concat (drop n %2) (take n %2)))
  (fn [n coll]
    (let [[f s] (split-at (mod n (count coll)) coll)]
      (concat s f))))

(defn flip-out
  "Problem 46, Flipping out"
  [f]
  #(f %2 %1))

(defn split-by-type
  "Problem 50, Split by Type"
  [coll]
  (vals (group-by type coll)))

(defn longest-incr-subs
  "Problem 53, Longest Increasing Sub-Seq"
  [coll]
  (->>
   (reduce
    (fn [res curr]
      (if (= (inc (last res)) curr)
        (conj res curr)
        (conj res :split curr)))
    [(first coll)]
    coll)
   (partition-by #(= % :split))
   (filter #(> (count %) 1))
   (sort-by count)
   last
   (#(or % []))))

(defn my-partition
  "Problem 54, Partition a Sequence"
  [n coll]
  (loop [result [] coll-left coll]
    (let [curr (take n coll-left)]
      (if (< (count curr) n)
        result
        (recur (conj result curr) (drop n coll-left))))))

(defn count-occurences
  "Problem 55, Count Occurences"
  [coll]
  (reduce (fn [res [group all-grouped]] (assoc res group (count all-grouped))) {} (group-by identity coll)))

(comment
  ; nice one
  (fn [x] (reduce #(assoc %1 %2 (inc (%1 %2 0))) {} x)))

(defn my-distinct
  "Problem 56, Find Distinct Items"
  [coll]
  (reduce (fn [res curr] (if (some #{curr} res) res (conj res curr))) [(first coll)] (rest coll)))

(defn my-comp
  "Problem 58, Function Composition"
  [& fns]
  (let [[f1 & frest] (reverse fns)]
    (fn [& args] (reduce #(%2 %1) (apply f1 args) frest))))

(defn my-juxt
  "Problem 59, Juxtaposition"
  [& fns]
  (fn [& args]
    (map #(apply % args) fns)))
