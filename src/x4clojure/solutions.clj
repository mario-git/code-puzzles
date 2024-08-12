(ns x4clojure.solutions)

; Solutions to 4clojure problems. Not all of them, skipping trivial ones

; Problem 26, Fibonacci Sequence
(defn fibo [n]
  (loop [idx n results []]
    (if (zero? idx)
      (into () results)
      (let [next-fibo (apply + (take 2 (or (seq results) '(1))))]
        (recur (dec idx) (cons next-fibo results))))))

(defn solution26 [n] (fibo n))

(comment
; clever solution, assumes result starting from 0

  (def fibs (lazy-cat [0N 1N] (map + fibs (rest fibs)))))
