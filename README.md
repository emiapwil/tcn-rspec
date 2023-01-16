

## Basic Concepts

~~~
module 
- variable (private/public)
  - classifier (set of pipes)
    - attribute: examples - project, activity, src_rse, dst_rse, sip, dip
    - composition:
      - projection
      - &, |, \, !
  - resource
    - attribute: examples - router (ip/CNAME), ingress/egress, capacity
    - &, |
    - +, -, * c, / c (linear composition)
  - policy
    - expr <= expr, expr >= expr <- absolute
    - expr : expr = constant : constant <- relative
    - expr := classifier @ resource
      -> sum of the usage of the resource by all pipes in classifier
           | expr + expr
           | expr - expr
           | expr * const | const * expr
           | expr / non-zero const
           | const
           | conf configfile entry
           | db serverip table ...
      -> linear composition of expr

-> all policies are linear constraints on T
  
~~~
