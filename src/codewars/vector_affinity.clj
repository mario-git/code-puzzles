(ns codewars.vector-affinity)

(defn vector-affinity
  [a b]
  (if (= a b) 1.0
      (->> (map vector a b)
           (filter #(= (first  %) (second  %)))
           (count)
           (#(/ % (max (count a) (count b))))
           (float))))
