(ns codewars.dir-reduc)

(defn- opposites? [x y]
  (and (not= x y)
       (or
        (= #{"NORTH" "SOUTH"} #{x y})
        (= #{"EAST" "WEST"} #{x y}))))

(defn- dirReducStep [arr item]
  (if (opposites? (last arr) item)
     (pop arr)
     (conj arr item)))

(defn dirReduc
  [arr]
  (not-empty (reduce dirReducStep [] arr)))
