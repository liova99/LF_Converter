Java Basics
===========

Useful intellij idea shurtcuts
------------------------------

.. code:: java

    sout - just print System.out.println()

    soutm - added Class name & method name

    soutp - added parameter

    soutv - added last variable name

Hello World
-----------

.. code:: java

    package test;

    class helloworld {
        
    // This is Java's built-in main method! 
            public static void main(String args[]){
                System.out.println("hello World");
                double tuna;
                tuna = 5.28;
                System.out.print(tuna);
        }

System.out.println will print the next print on a new line where
System.out.print will print at the same line.

.. code:: java

    System.out.print('Levan is ');
    System.out.println('Great');
    System.out.print('man');
    // -------Console--------- //
    Levan is Great
    man
