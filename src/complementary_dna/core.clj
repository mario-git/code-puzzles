(ns complementary-dna.core)

(def ^:private complements
  {\A \T \C \G \G \C \T \A})

(defn dna-strand [dna]
  (->> dna
       (map #(complements %))
       (apply str)))
