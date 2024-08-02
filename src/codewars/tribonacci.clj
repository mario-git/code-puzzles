(ns codewars.tribonacci)

(defn tribonacci [[a b c] n]
  (loop [result [a b c]
         loops-left n]
    (if (zero? loops-left)
      (take n result)
      (recur (conj result (apply + (take-last 3 result)))
             (dec loops-left)))))
