*Replace the bold text with your own content*

*Adapted from https://htdp.org/2020-5-6/Book/part_preface.html*

# 0.  From Problem Analysis to Data Definitions

**Problem Analysis is the process of understanding the problem the software
will address and to document in detail what the software system needs to do.
In the real world this phase demands close interaction between developers and
the client.  Ideally, end-users of the system are interviewed for their input.**

**In this course you will receive detailed requirements in the form of the
assignment description.  I stand-in for the client and end-users when you have
questions concerning their needs and desires.**

**In this phase of the design process you should use [The Feynman
Technique](https://www.youtube.com/watch?v=tkm0TNFzIeg) To ensure that you
understand what is being asked of you.**

**The output of this phase of the development process is a restatement of the
requirements in your own words.  Putting new problems into your own words will
help you identify your "Known knowns" and your "known unknowns".**

**As part of your restatement of the problem identify information that must be
represented and decide how to represent in the chosen programming language.**

**Formulate data definitions and illustrate them with examples.**


# 1.  System Analysis

**Analyze the flow of data throughout the program.  Does the program get input
from the user?  If so, does it come from interactive prompts or from
command-line arguments?  Is data incorporated from a file on the disk, from a
database or from the internet?**

**How is output given?  On the screen in the form of text or graphics?  Are
output files created, and what form do they take?**

**Identify the non-trivial formulas you need to create.  If there aren't any then
state "no formulas" in this section.**

**State what kind of data each desired function consumes and produces.  Formulate
a concise description of what the function computes.  Define a stub that lives
up to the signature.**


# 2.  Functional Examples

**Design a process for obtaining the output from the input.  Consider both *good*
and *bad* inputs.  Find or create examples of both kinds of input.**

**Work out problem examples on paper, on a whiteboard or some other medium that
is *not* your computer.  It is a mistake to begin writing executable code
before you thoroughly understand what form the algorithm(s) must take.**

**Instead, describe components of the system in *"pseudocode"*.  Expect to make
lots of mistakes at this point.  You will find that it is much easier to throw
away pseudocode than real code.**

**Manually work through several examples that illustrate the program's overall
purpose, as well as the purpose of each component of the finished system.  You
will converge on a correct solution much faster if you feel comfortable making
mistakes as you go.**

**This phase involves the use of many levels of abstraction to decompose the
problem into manageable components, and design strategies for implementing each
component.  Components may be functions, modules or classes.**


# 3.  Function Template

**Combine the function stubs written in step #2 with pseudocode from step #3.
Comment out the pseudocode, leaving a valid program that compiles/runs without
errors.  At this stage your program doesn't quite work, but it also doesn't
crash.**


# 4.  Implementation

**This is the only part of the process focused on writing code in your chosen
programming language.**

**One by one translate passages of pseudocode into valid code.  Fill in the gaps
in the function template.  Exploit the purpose statement and the examples.**

**If you were thorough in the previous steps and are familiar with your
programming system this part will go by very quickly and the code will write
itself.**

**When you are learning a new programming language or an unfamiliar library this
phase can be slow and difficult.  As you gain experience with the relevant
technologies you will spend less and less time in this phase of the process.**


# 5.  Testing

**Articulate the examples given in step #2 as tests and ensure that each
function passes all of its tests.  Doing so discovers mistakes.  Tests also
supplement examples in that they help others read and understand the definition
when the need arises—and it will arise for any serious program.**

**As bugs are discovered and fixed, devise new test cases that will detect these
problems should they return.**

**If you didn't come across any bugs (lucky you!) think of a possible flaw and a
test that can be employed to screen for it.**

**At a minimum you should create a document explaining step-by-step how a
non-technical user may manually test your program to satisfy themselves that it
operates correctly.  Explain the entire process starting how to launch the
program, what inputs they should give and what results they should see at every
step.  Provide test cases of good and bad inputs to catch both false positives
and false negatives.  Any deviation from the expected outputs are errors.**

**The ideal is to write an automated test to avoid all manual labor beyond
launching the test.**
