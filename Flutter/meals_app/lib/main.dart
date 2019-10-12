import 'package:flutter/material.dart';

import './screens/tabs_screen.dart';
import './screens/cateogry_meals_screen.dart';
import './screens/single_meal_detail.dart';
import './screens/filters_screen.dart';

import './dummy-data.dart';
import './models/recipes.dart';

void main() => runApp(MyApp());

class MyApp extends StatefulWidget {
  // This widget is the root of your application.
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  Map<String, bool> _filters = {
    'gluten': false,
    'lactose': false,
    'vegan': false,
    'vegeterian': false
  };

  List<Recipe> _availableMeals = DUMMY_MEALS;
  List<Recipe> _favoriteMeals = [];

  void _toogleFavorite(String mealId) {
    final existingIndex =
        _favoriteMeals.indexWhere((meal) => meal.id == mealId);
    if (existingIndex >= 0) {
      setState(() {
        _favoriteMeals.removeAt(existingIndex);
      });
    } else {
      setState(() {
        _favoriteMeals.add(DUMMY_MEALS.firstWhere((meal) => meal.id == mealId));
      });
    }
  }

  void _setFilters(Map<String, bool> _newFilters) {
    setState(() {
      _filters = _newFilters;
    });
    _availableMeals = DUMMY_MEALS.where((meal) {
      if (_filters['gluten'] && !meal.isGlutenFree) {
        return false;
      }
      if (_filters['lactose'] && !meal.isLactoseFree) {
        return false;
      }
      if (_filters['vegan'] && !meal.isVegan) {
        return false;
      }
      if (_filters['vegeterian'] && !meal.isVegetarian) {
        return false;
      }
      return true;
    }).toList();
  }

  bool _isFavorite(String mealId) {
    return _favoriteMeals.any((meal) => meal.id == mealId);
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'MealNow',
      theme: ThemeData(
          primarySwatch: Colors.indigo,
          accentColor: Colors.orange,
          // canvasColor: Color.fromRGBO(255, 254, 229, 1),
          fontFamily: 'Raleway',
          textTheme: ThemeData.light().textTheme.copyWith(
              body1: TextStyle(color: Color.fromRGBO(20, 51, 51, 1)),
              body2: TextStyle(color: Color.fromRGBO(20, 51, 51, 1)),
              title: TextStyle(
                  fontSize: 20,
                  fontFamily: 'RobotoCondensed',
                  fontWeight: FontWeight.bold))),
      initialRoute: '/',
      routes: {
        '/': (ctx) => TabsScreen(_favoriteMeals),
        CategoryMealsScreen.routeName: (ctx) =>
            CategoryMealsScreen(_availableMeals),
        SingleMealDetail.routeName: (ctx) =>
            SingleMealDetail(_toogleFavorite, _isFavorite),
        FilterScreen.routeName: (ctx) => FilterScreen(_filters, _setFilters)
      },
      // onGenerateRoute: (settings){
      //   if(settings.name == '/'){
      //     return CategoriesScreen()
      //   } else {
      //     return CategoryMealsScreen()
      //   }
      // },
    );
  }
}
