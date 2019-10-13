import 'package:flutter/material.dart';
import '../widgets/meal_item.dart';
import '../dummy-data.dart';
import '../models/recipes.dart';

class CategoryMealsScreen extends StatelessWidget {
  static final routeName = '/categoy-meals';
  // final String categoryId;
  // final String categoryTitle;
  // final Color categoryColor;
  final List<Recipe> _availableMeals;

  CategoryMealsScreen(this._availableMeals);

  @override
  Widget build(BuildContext context) {
    final routeArgs =
        ModalRoute.of(context).settings.arguments as Map<String, String>;
    final categoryTitle = routeArgs['title'];
    final categoryId = routeArgs['id'];
    final categoryMeals = _availableMeals.where((item) {
      return item.categories.contains(categoryId);
    }).toList();

    return Scaffold(
        backgroundColor: Colors.white,
        appBar: AppBar(
          leading: IconButton(
            icon: Icon(
              Icons.arrow_back_ios,
              color: Colors.black,
            ),
            onPressed: () => Navigator.of(context).pop(),
          ),
          elevation: 0,
          centerTitle: true,
          backgroundColor: Colors.white,
          title: Text(
            categoryTitle,
            style: TextStyle(color: Colors.black),
          ),
        ),
        body: Padding(
          padding: const EdgeInsets.symmetric(vertical: 20.0),
          child: ListView.builder(
              itemCount: categoryMeals.length,
              itemBuilder: (ctx, index) {
                return MealItem(
                  id: categoryMeals[index].id,
                  title: categoryMeals[index].title,
                  imageUrl: categoryMeals[index].imageUrl,
                  duration: categoryMeals[index].duration,
                  affordability: categoryMeals[index].affordability,
                  complexity: categoryMeals[index].complexity,
                );
              }),
        ));
  }
}
