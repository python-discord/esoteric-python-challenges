
h =                    (lambda n:(lambda               o=int(.5*n//1):
                    [([(                lambda   m=(x/n             *3),l=(
                  y / n                   *3):  print              ([" ","#"
                    ][(                      m**2                   +l**2
                     -1)                                            **3
                      -m**2                                        *l
                        **3                                       <0
                         ],end                                  =""
                          ))                                   ()
                            for                              x in
                              range                        (-o,
                                o)]                     ,print
                                  ())                  for
                                    y                 in
                                     range          (o,
                                        -o,       -1
                                          )]     )(
                                             ))


if __name__ == "__main__":
    h(10)
    h(50)
    h(100)
