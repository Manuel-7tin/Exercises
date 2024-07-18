# Exercises
Attribute: [Angela Yu](https://www.linkedin.com/in/angela-yu1/?originalSubdomain=uk) | [Appbrewery](https://appbrewery.com/)


e^x & \sin 2x & \sin x \\
e^x & 2 \cos 2x & \cos x \\
e^{2x} & -4 \sin 2x & -\sin x
\end{vmatrix} \]
### Step-by-Step Calculation
#### Step 1: Write the Determinant in Matrix Form
\[ W(x) = \begin{vmatrix}
e^x & \sin 2x & \sin x \\
e^x & 2 \cos 2x & \cos x \\
e^{2x} & -4 \sin 2x & -\sin x
\end{vmatrix} \]
#### Step 2: Expand the Determinant
Expand along the first row:
\[ W(x) = e^x \begin{vmatrix}
2 \cos 2x & \cos x \\
-4 \sin 2x & -\sin x
\end{vmatrix}
- \sin 2x \begin{vmatrix}
e^x & \cos x \\
e^{2x} & -\sin x
\end{vmatrix}
+ \sin x \begin{vmatrix}
e^x & 2 \cos 2x \\
e^{2x} & -4 \sin 2x
\end{vmatrix} \]
#### Step 3: Calculate the 2x2 Determinants
1. First 2x2 determinant:
\[ \begin{vmatrix}
2 \cos 2x & \cos x \\
-4 \sin 2x & -\sin x
\end{vmatrix}
= (2 \cos 2x \cdot -\sin x) - (\cos x \cdot -4 \sin 2x) \]
\[ = -2 \cos 2x \sin x + 4 \sin 2x \cos x \]
2. Second 2x2 determinant:
\[ \begin{vmatrix}
e^x & \cos x \\
e^{2x} & -\sin x
\end{vmatrix}
= (e^x \cdot -\sin x) - (\cos x \cdot e^{2x}) \]
\[ = -e^x \sin x - e^{2x} \cos x \]
3. Third 2x2 determinant:
\[ \begin{vmatrix}
e^x & 2 \cos 2x \\
e^{2x} & -4 \sin 2x
\end{vmatrix}
= (e^x \cdot -4 \sin 2x) - (2 \cos 2x \cdot e^{2x}) \]
\[ = -4 e^x \sin 2x - 2 e^{2x} \cos 2x \]
#### Step 4: Combine the Results
Now substitute back into the expanded determinant:
\[ W(x) = e^x \left( -2 \cos 2x \sin x + 4 \sin 2x \cos x \right)
- \sin 2x \left( -e^x \sin x - e^{2x} \cos x \right)
+ \sin x \left( -4 e^x \sin 2x - 2 e^{2x} \cos 2x \right) \]
#### Step 5: Simplify the Expression
\[ W(x) = e^x \left( -2 \cos 2x \sin x + 4 \sin 2x \cos x \right)
+ \sin 2x e^x \sin x + \sin 2x e^{2x} \cos x
+ \sin x \left( -4 e^x \sin 2x - 2 e^{2x} \cos 2x \right) \]
Combine like terms and simplify further if possible:
\[ W(x) = e^x (-2 \cos 2x \sin x + 4 \sin 2x \cos x + \sin 2x \sin x - 4 \sin x \sin 2x)
+ e^{2x} (\sin 2x \cos x - 2 \sin x \cos 2x) \]
\[ W(x) = e^x \left( -2 \cos 2x \sin x + 4 \sin 2x \cos x + \sin 2x \sin x - 4 \sin x \sin 2x \right)
+ e^{2x} \left( \sin 2x \cos x - 2 \sin x \cos 2x \right) \]
Simplify each term separately:
\[ W(x) = e^x \left( -2 \cos 2x \sin x + 4 \sin 2x \cos x + \sin 2x \sin x - 4 \sin x \sin 2x \right) \]
\[ W(x) = e^{2x} \left( \sin 2x \cos x - 2 \sin x \cos 2x \right) \]
Combine like terms:
\[ W(x) = e^x \left( -2 \cos 2x \sin x + 4 \sin 2x \cos x + \sin 2x \sin x - 4 \sin x \sin 2x \right) \]
\[ W(x) = e^{2x} \left( \sin 2x \cos x - 2 \sin x \cos 2x \right) \]
Finally, we can simplify the resulting expression to obtain the final form of the Wronskian \( W(x) \).
