import Recognize as R
import clojure_2450 as Main

import sys
if __name__ == '__main__':
    R.main('./lang/clojure/grammar/clojure.fbjson', './lang/clojure/bugs/clj-2450.clj', Main.my_predicate)
