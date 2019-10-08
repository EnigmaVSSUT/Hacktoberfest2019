import React, { useState, useEffect } from 'react'

const ThemeToggler = () => {
  const [theme, setTheme] = useState('light')

  const toggleTheme = () => {
    if (theme === 'light') {
      document.documentElement.setAttribute('data-theme', 'dark')
      localStorage.setItem('theme', 'dark')
      setTheme('dark')
    } else {
      document.documentElement.setAttribute('data-theme', 'light')
      localStorage.setItem('theme', 'light')
      setTheme('light')
    }
  }

  useEffect(() => {
    const localTheme = localStorage.getItem('theme')
    if (localTheme) {
      document.documentElement.setAttribute('data-theme', localTheme)
      setTheme(localTheme)
    }
  })

  return (
    <button type="button" onClick={toggleTheme}>
      Toggle Theme
    </button>
  )
}

export default ThemeToggler
