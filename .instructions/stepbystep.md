## Step by step instructions


> NOTE: You're welcome to follow along using these steps but we have a guided CodeTour option that displays the instructions directly in the VSCode editor if you prefer. To use the CodeTour, follow the instructions in the [Using-CodeTour](./using-codetour.md) file.
---
:bulb:  When you see the :leftwards_arrow_with_hook: symbol, you need to press the ENTER key.


1. For our exercises, you'll get started by navigating to the appropriate repo and choosing '**Use this template**', and '**Open in a codespace**'

<img width="601" alt="Open in a Codespace" src="../assets/Open in a Codespace.png">



2. Ensure you can see the files in the **Explorer view**. If not, click the **Explorer View icon** on the left sidebar of your editor.

<img width="398" alt="Code Explorer View" src="../assets/Code Explorer View.png">

3. Open the ```main.py``` file if it's not already open in the editor.
4. Let's start by adding the following comment to provide some context for the code we're about to write:
```# Write a rock, paper, scissors game``` :leftwards_arrow_with_hook:

5. On the next line we're going to prompt GitHub Copilot to suggest code for us by typing the following:

```# import random module``` :leftwards_arrow_with_hook:

6. When you press **Enter** after typing the previous comment, GitHub Copilot will suggest some code for you. Select the first suggestion by pressing **TAB** then **Enter** again.


<img width="529" alt="Copilot Suggestion - Import Random" src="../assets/Copilot Suggestion - Import Random.png">

7. Now we're going to prompt GitHub Copilot to suggest code for us by typing the following:

```# define main function that handles all the logic``` :leftwards_arrow_with_hook:

8. When you press **Enter** after typing the previous comment, GitHub Copilot will again suggest some code for you. Select the first suggestion by pressing **TAB** then **Enter** again.
9. **Pause briefly** while Copilot creates up to 10 suggestions for you. You should see the Copilot icon in the lower right corner of the editor spinning. When Copilot displays the first suggestion, we're going to open the GitHub Copilot suggestion panel by pressing **CTRL + ENTER**. 
10. Scroll down the list of suggestions that GitHub Copilot has made and choose the one that looks like the best option for our Rock, Paper, Scissors game. When you see the suggestion you want, click **Accept Solution** to have that code snippet inserted into your code file.

<img width="906" alt="Copilot Suggestion - Accept Solution" src="../assets/Copilot Suggestion - Accept Solution.png">


11. On the line following the last snippet, let's prompt GitHub Copilot to suggest the final line of code for us by typing the following:

```# call main function``` :leftwards_arrow_with_hook:

12. When you press Enter after typing the previous comment, GitHub Copilot will suggest some code for you. Select the first suggestion by pressing TAB then Enter again.

<img width="498" alt="Copilot Suggestion - def main" src="../assets/Copilot Suggestion - def main.png">


**Now we're ready to see if this code executes** :thumbsup:

13. In the Terminal window in your Codespace, type the following command and press **Enter** to run the code:

```python3 main.py``` :leftwards_arrow_with_hook:

Here's an example of what the completed game might look like.

<img width="645" alt="Running the game" src="../assets/Running the game.png">


---
### Wrap up

Hopefully your Paper, Rock, Scissors game is working! Remember, GitHub Copilot is probabilistic so you may not get the exact same code suggestions as we did. If you're not happy with the suggestions, you can always press **CTRL + Z** to undo the changes and try again.


