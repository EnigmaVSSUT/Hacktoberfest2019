(defn fact
  [x] 
  (reduce * (range 1 (inc x))))
