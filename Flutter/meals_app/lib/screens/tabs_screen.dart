import 'package:flutter/material.dart';
import './categories_screen.dart';
import './favorites_screen.dart';
import '../widgets/main_drawer.dart';
import '../models/recipes.dart';

class TabsScreen extends StatefulWidget {
  final List<Recipe> _favoriteMeals;
  TabsScreen(this._favoriteMeals);

  @override
  _TabsScreenState createState() => _TabsScreenState();
}

class _TabsScreenState extends State<TabsScreen> {
  final GlobalKey<ScaffoldState> _scaffoldKey = new GlobalKey<ScaffoldState>();

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 2,
      child: Scaffold(
        backgroundColor: Colors.white,
        key: _scaffoldKey,
        drawer: MainDrawer(),
        appBar: AppBar(
          elevation: 0,
          actions: <Widget>[
            IconButton(
              icon: Icon(Icons.search),
              iconSize: 20,
              onPressed: () {},
              color: Colors.black,
            )
          ],
          leading: IconButton(
            icon: Icon(Icons.menu),
            iconSize: 20,
            color: Colors.black,
            onPressed: () => _scaffoldKey.currentState.openDrawer(),
          ),
          backgroundColor: Colors.white,
          bottom: TabBar(
            labelColor: Colors.black,
            indicatorSize: TabBarIndicatorSize.label,
            indicatorColor: Colors.black,
            unselectedLabelColor: Color(0xffcccccc),
            tabs: <Widget>[
              Tab(
                icon: Icon(Icons.category),
                text: 'Categoires',
              ),
              Tab(icon: Icon(Icons.favorite), text: 'Favorites')
            ],
          ),
        ),
        body: TabBarView(
          children: <Widget>[
            CategoriesScreen(),
            FavoriteScreen(widget._favoriteMeals),
          ],
        ),
      ),
    );
  }
}
