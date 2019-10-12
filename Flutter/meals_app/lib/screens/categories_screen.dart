import 'package:flutter/material.dart';

import '../widgets/category_item.dart';
import '../dummy-data.dart';

class CategoriesScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.spaceAround,
      children: <Widget>[
        Container(
          margin: EdgeInsets.symmetric(vertical: 50, horizontal: 30),
          alignment: Alignment.centerLeft,
          child: Container(
            child: Text(
              'MEALS NOW',
              style: TextStyle(
                  letterSpacing: 10,
                  color: Colors.black,
                  fontSize: 30,
                  fontWeight: FontWeight.bold),
            ),
          ),
        ),
        Expanded(
          flex: 5,
          child: GridView(
            scrollDirection: Axis.horizontal,
            padding: const EdgeInsets.all(25),
            children: DUMMY_CATEGORIES.map((catData) {
              return CategoryItem(catData.title, catData.color, catData.id);
            }).toList(),
            gridDelegate: SliverGridDelegateWithMaxCrossAxisExtent(
                maxCrossAxisExtent: 400,
                childAspectRatio: 1,
                mainAxisSpacing: 25),
          ),
        ),
      ],
    );
  }
}
