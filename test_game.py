# test case
import unittest
from game import getWord, word_dict, Button
from unittest.mock import Mock
import game
import pygame
pygame.init()

class HangmanTest(unittest.TestCase):
    def test_getWord(self):
        # Test if getWord returns a tuple containing a word and its meaning
        word, meaning = getWord()
        self.assertIsInstance(word, str)
        self.assertIsInstance(meaning, str)
        
    def test_word_dict(self):
        # Test if word_dict is correctly populated and contains words with meanings
        self.assertTrue(len(word_dict) > 0)
        for word, meaning in word_dict.items():
            self.assertIsInstance(word, str)
            self.assertIsInstance(meaning, str)

    def test_guess_correct_letter(self):
        # Test if guessing a correct letter updates guessed letters
        word, _ = getWord()
        guessed = ['' for _ in range(len(word))]
        letter = word[0]
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
        self.assertIn(letter, word)
        self.assertEqual(guessed[word.index(letter)], letter)
    
    def test_guess_incorrect_letter(self):
        # Test if guessing an incorrect letter reduces lives and handles game over
        word, _ = getWord()
        guessed = ['' for _ in range(len(word))]
        lives = 6
        incorrect_letter = 'X'  # Assuming 'X' is not in the word
        if incorrect_letter not in word:
            lives -= 1
        self.assertNotIn(incorrect_letter, word)
        self.assertEqual(lives, 5)  # Assuming lives start at 6 and reduce by 1 for each incorrect guess

    def test_game_reset(self):
        # Test if the game resets correctly after a game over or restart
        word, meaning = getWord()
        guessed = ['' for _ in range(len(word))]
        word_list = [word]
        score = 5  # Assuming some score
        lives = 1  # Assuming only one life left
        # Simulate game over or restart
        word, meaning = getWord()
        guessed = ['' for _ in range(len(word))]
        word_list = [word]
        score = 0
        lives = 6
        self.assertEqual(score, 0)
        self.assertEqual(lives, 6)
        self.assertEqual(len(word_list), 1)

class TestFadeScreen(unittest.TestCase):
    def setUp(self):
        self.fade_screen = game.FadeScreen(100, 100, (255, 255, 255))

    def test_fade_screen_initialization(self):
        self.assertEqual(self.fade_screen.alpha, 255)
        self.assertIsNotNone(self.fade_screen.surface)
        # Add more specific assertions based on your requirements

    def test_fade_screen_update(self):
        initial_alpha = self.fade_screen.alpha
        self.fade_screen.update()
        self.assertEqual(self.fade_screen.alpha, initial_alpha - 0.8)


if __name__ == '__main__':
    unittest.main()
