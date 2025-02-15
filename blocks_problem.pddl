(define (problem blocks-problem)
  (:domain blocks)
  (:objects 
    A B C - block
    agent1 - agent
  )
  (:init 
    (on-table A)
    (on-table B)
    (clear A)
    (clear B)
    (handempty agent1)
  )
  (:goal 
    (and 
      (on A B)
    )
  )
)