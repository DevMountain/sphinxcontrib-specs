Overview
========

Now that you're set up, let's get an overview of React!

Inspecting the starter code
---------------------------

In VS Code you'll see three main sections:

#. The `Explorer` section where you'll see...

#. The `Editor` section where you'll see the source code of your selected file.

#. The `Terminal` section where...

To get acquainted with VS Code, open the `src/App.js` file. The contents of the file in
`Editor` should be:

.. literalinclude:: ./starter-code/tic-tac-toe/src/App.js
   :language: jsx

In your browser, you should see

Now let's have a look at the files in the starter code, starting with the `*.js` files in
the `src/` folder.

`App.js`
++++++++

The code in `App.js` creates a :term:`component`. In React, a component is a piece of reusable
code that represents a part of a user interface. Components are used to render, manage,
and update the UI elements in your application. Let's look at the component line by line
to see what's going on:

.. literalinclude:: ./starter-code/tic-tac-toe/src/App.js
   :language: jsx
   :start-at: export
   :emphasize-lines: 1

The first line defines a function called `Square`. The `export` JavaScript keyword makes
this function accessible outside of this file. The default keyword tells other files
using your code that it's the main function in your file.

.. literalinclude:: ./starter-code/tic-tac-toe/src/App.js
   :language: jsx
   :start-at: export
   :emphasize-lines: 2

The second line returns a button. The `return` JavaScript keyword means whatever
comes after is returned as a value to the caller of the function. ``<button>`` is a
`JSX element`. A JSX element is a combination of JavaScript code and HTML tags that
describes what you'd like to display. ``className="square"`` is a button property
or `prop` that tells CSS how to style the button. ``X`` is the text displayed
inside of the button and ``</button>`` closes the JSX element to indicate that any
following content shouldn't be placed inside the button.

`styles.css`
++++++++++++

Open `src/styles.css` in the :guilabel:`Explorer` section of VS Code. This file defines the
styles for your React app.

The first two CSS selectors (``*`` and ``body``) define the style of large parts of
your app while the ``.square`` selector defines the style of any component where
the `className` property is set to `square`. In your code, that would match the
button from your `Square` component in the `App.js` file.

`index.js`
++++++++++

:kbd:`Enter`

Now open `src/index.js`. You won't be editing this file during the tutorial but it
is the bridge between the component you created in the `App.js` file and the web
browser.

.. literalinclude:: ./starter-code/tic-tac-toe/src/index.js
   :language: jsx
   :end-at: import App from "./App";

Lines 1--5 brings all the necessary pieces together:

- React

- React's library to talk to web browsers (React DOM)

- the styles for your components

- the component you created in `App.js`

The remainder of the file brings all the pieces together and injects the final product into `public/index.html`.

Building the board
-------------------

Let's get back to `App.js`. This is where you'll spend the rest of the tutorial.

Currently the board is only a single square, but you need nine! If you just try and copy
paste your square to make two squares like this:

.. code-block:: jsx
   :emphasize-lines: 2

   export default function Square() {
     return <button className="square">X</button><button className="square">X</button>;
   }

You'll get this error:

.. parsed-literal::

   /src/App.js: Adjacent JSX elements must be wrapped in an enclosing tag. Did you want a JSX fragment <>...</>?

React components need to return a single JSX element and not multiple adjacent JSX
elements like two buttons. To fix this you can use fragments (``<>`` and ``</>``) to wrap
multiple adjacent JSX elements like this:

.. code-block:: jsx
   :emphasize-lines: 3-6

   export default function Square() {
     return (
       <>
         <button className="square">X</button>
         <button className="square">X</button>
       </>
     );
   }
