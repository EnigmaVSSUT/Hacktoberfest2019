import 'package:flutter/material.dart';

import '../screens/cateogry_meals_screen.dart';

class CategoryItem extends StatelessWidget {
  final String id;
  final String title;
  final Color color;

  CategoryItem(this.title, this.color, this.id);

  void selectCategory(BuildContext context) {
    Navigator.of(context).pushNamed(CategoryMealsScreen.routeName,
        arguments: {'id': id, 'title': title});
  }

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: () => selectCategory(context),
      splashColor: Theme.of(context).primaryColor,
      borderRadius: BorderRadius.circular(10),
      child: Container(
        alignment: Alignment.center,
        padding: const EdgeInsets.all(15),
        child: Text(
          title,
          style: TextStyle(color: Colors.white, fontSize: 24),
        ),
        decoration: BoxDecoration(
            boxShadow: [
              new BoxShadow(
                color: Color(0xffcccccc),
                offset: new Offset(5.0, 5.0),
                blurRadius: 5.0,
              )
            ],
            gradient: LinearGradient(
                colors: [color.withOpacity(0.8), color],
                begin: Alignment.topLeft,
                end: Alignment.bottomRight),
            borderRadius: BorderRadius.circular(10)),
      ),
    );
  }
}

//ANimated Navigation

// Route _createRoute() {
//   return PageRouteBuilder(
//     pageBuilder: (context, animation, secondaryAnimation) =>
//         CategoryMealsScreen(),
//     transitionsBuilder: (
//       BuildContext context,
//       Animation<double> animation,
//       Animation<double> secondaryAnimation,
//       Widget child,
//     ) =>
//         Align(
//       child: SizeTransition(
//         sizeFactor: animation,
//         child: child,
//       ),
//     ),
//   );
// }
