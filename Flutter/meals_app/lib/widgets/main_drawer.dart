import 'package:flutter/material.dart';
import '../screens/filters_screen.dart';

class MainDrawer extends StatelessWidget {
  Widget _buildListTile(IconData iconData, String title, Function tapHandler) {
    return ListTile(
      leading: Icon(
        iconData,
        size: 24,
        color: Colors.black,
      ),
      title: Text(
        title,
        style: TextStyle(fontSize: 24),
      ),
      onTap: tapHandler,
    );
  }

  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: Column(
        children: <Widget>[
          Container(
            child: Text(
              'Cooking Time!',
              style: TextStyle(
                  color: Colors.white,
                  fontSize: 30,
                  fontWeight: FontWeight.w700),
            ),
            height: 200,
            color: Colors.red,
            alignment: Alignment.center,
          ),
          SizedBox(
            height: 20,
          ),
          _buildListTile(Icons.restaurant, 'Meals', () {}),
          _buildListTile(Icons.settings, 'Filters',
              () => Navigator.pushNamed(context, FilterScreen.routeName))
        ],
      ),
    );
  }
}
