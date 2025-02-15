(define (domain blocks)
  (:requirements :strips)

  ;; Declare object types
  (:types block agent)

  ;; Declare predicates
  (:predicates
    (on ?x - block ?y - block)
    (clear ?x - block)
    (on-table ?x - block)
    (holding ?x - block)
    (handempty ?a - agent)
  )

  ;; Define actions
  (:action pick-up
    :parameters (?x - block ?a - agent)
    :precondition (and (clear ?x) (on-table ?x) (handempty ?a))
    :effect (and (not (clear ?x)) (not (on-table ?x)) (not (handempty ?a)) (holding ?x))
  )

  (:action put-down
    :parameters (?x - block ?a - agent)
    :precondition (and (holding ?x) (handempty ?a))
    :effect (and (clear ?x) (on-table ?x) (handempty ?a) (not (holding ?x)))
  )

  (:action stack
    :parameters (?x - block ?y - block ?a - agent)
    :precondition (and (holding ?x) (clear ?y))
    :effect (and (not (holding ?x)) (not (clear ?y)) (clear ?x) (on ?x ?y))
  )

  (:action unstack
    :parameters (?x - block ?y - block ?a - agent)
    :precondition (and (clear ?x) (on ?x ?y) (handempty ?a))
    :effect (and (holding ?x) (clear ?y) (not (on ?x ?y)) (not (clear ?x)))
  )
)