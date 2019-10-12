import 'package:flutter/material.dart';
import '../models/recipes.dart';
import '../widgets/meal_item.dart';

class FavoriteScreen extends StatelessWidget {
  final List<Recipe> _favoriteMeals;
  FavoriteScreen(this._favoriteMeals);

  @override
  Widget build(BuildContext context) {
    if (_favoriteMeals.isEmpty) {
      return Center(
        child: Text('Add some Favorites'),
      );
    } else {
      return ListView.builder(
          itemCount: _favoriteMeals.length,
          itemBuilder: (ctx, index) {
            return MealItem(
              id: _favoriteMeals[index].id,
              title: _favoriteMeals[index].title,
              imageUrl: _favoriteMeals[index].imageUrl,
              duration: _favoriteMeals[index].duration,
              affordability: _favoriteMeals[index].affordability,
              complexity: _favoriteMeals[index].complexity,
            );
          });
    }
  }
}
