import 'package:chatbot_app/core/constants/data.dart';
import 'package:chatbot_app/core/widgts/custom_button.dart';
import 'package:chatbot_app/features/chat/chat_screen.dart';
import 'package:flutter/material.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  ValueNotifier<int> currentIndex = ValueNotifier(0);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: EdgeInsets.only(top: 38, left: 16, right: 16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisSize: MainAxisSize.min,
              children: [
                SizedBox(
                  width: MediaQuery.of(context).size.width,
                  child: Row(
                    children: [
                      Container(
                        width: 38,
                        height: 38,
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(50),
                        ),
                        child: ClipRRect(
                          borderRadius: BorderRadius.circular(50),
                          child: Image.asset(
                            "assets/user.jpeg",
                            fit: BoxFit.cover,
                          ),
                        ),
                      ),
                      SizedBox(width: 10),
                      Text(
                        "John Doe",
                        style: TextStyle(
                          fontSize: 20,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      Spacer(),
                      IconButton(
                        onPressed: () {
                          print("Notifications");
                        },
                        icon: Icon(Icons.notifications_none_outlined, size: 30),
                      ),
                    ],
                  ),
                ),
                SizedBox(height: 20),

                // Balance
                Container(
                  padding: EdgeInsets.all(16),
                  width: double.infinity,
                  height: 200,
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(20),
                    gradient: LinearGradient(
                      begin: Alignment.bottomRight,
                      end: Alignment.topLeft,
                      colors: [Color(0xFF3F57C5), Color(0xFF0B0F49)],
                    ),
                    boxShadow: [
                      BoxShadow(
                        color: Color(0xFF123abc),
                        blurRadius: 10,
                        spreadRadius: 3,
                        offset: Offset(0, 10),
                      ),
                    ],
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      SizedBox(height: 10),
                      Text(
                        "Balance",
                        style: TextStyle(
                          fontSize: 20,
                          color: Colors.white.withValues(alpha: 0.8),
                        ),
                      ),
                      Text(
                        "\$214.12",
                        style: TextStyle(color: Colors.white, fontSize: 30),
                      ),
                      Spacer(),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                        children: [
                          customButton(
                            title: "Credit",
                            bgColor: Colors.white.withValues(alpha: 0.1),
                            textColor: Colors.white.withValues(alpha: 0.8),
                          ),

                          customButton(
                            title: "Debits",
                            bgColor: Colors.white.withValues(alpha: 0.1),
                            textColor: Colors.white.withValues(alpha: 0.8),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
                SizedBox(height: 50),

                // Services
                Text(
                  "Services",
                  style: TextStyle(fontSize: 20, fontWeight: FontWeight.w500),
                ),
                SizedBox(height: 10),
                SingleChildScrollView(
                  scrollDirection: Axis.horizontal,
                  child: Row(
                    children:
                        kServices.map((service) {
                          return Card(
                            elevation: 3,
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(12),
                            ),
                            child: Container(
                              width: 120,
                              height: 110,
                              padding: EdgeInsets.all(12),
                              decoration: BoxDecoration(
                                borderRadius: BorderRadius.circular(12),
                                color: service["color"].withValues(alpha: 0.15),
                              ),
                              child: Column(
                                mainAxisAlignment: MainAxisAlignment.center,
                                children: [
                                  Icon(
                                    service["icon"],
                                    color: service["color"],
                                    size: 30,
                                  ),
                                  const SizedBox(height: 10),
                                  Text(
                                    service["title"],
                                    style: TextStyle(
                                      fontSize: 16,
                                      fontWeight: FontWeight.w600,
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          );
                        }).toList(),
                  ),
                ),
                SizedBox(height: 30),
              ],
            ),

            // Recent transactions
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    "Recent Transactions",
                    style: TextStyle(fontSize: 20, fontWeight: FontWeight.w500),
                  ),
                  SizedBox(height: 5),
                  Expanded(
                    child: ListView.builder(
                      shrinkWrap: true,
                      itemCount: kTransactions.length,
                      itemBuilder: (context, index) {
                        final tx = kTransactions[index];

                        return Card(
                          margin: EdgeInsets.only(bottom: 10),
                          child: ListTile(
                            leading: CircleAvatar(child: Icon(tx["icon"])),
                            title: Text(tx["title"]),
                            subtitle: Text(tx["date"]),
                            trailing: Text(
                              tx["amount"],
                              style: TextStyle(
                                color:
                                    tx["type"] == "income"
                                        ? Colors.green
                                        : Colors.red,
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                          ),
                        );
                      },
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
      bottomNavigationBar: SizedBox(
        height: MediaQuery.of(context).size.height * 0.1,
        child: ValueListenableBuilder(
          valueListenable: currentIndex,
          builder: (context, value, child) {
            return BottomNavigationBar(
              currentIndex: value,
              type: BottomNavigationBarType.shifting,
              onTap: (index) {
                currentIndex.value = index;
              },
              selectedItemColor: Colors.black,
              unselectedItemColor: Colors.grey,
              elevation: 0,

              items: [
                BottomNavigationBarItem(icon: Icon(Icons.home), label: "Home"),
                BottomNavigationBarItem(
                  icon: Icon(Icons.history),
                  label: "History",
                ),
                BottomNavigationBarItem(
                  icon: Icon(Icons.settings),
                  label: "Settings",
                ),
              ],
            );
          },
        ),
      ),

      floatingActionButton: FloatingActionButton(
        backgroundColor: Color(0xFF3B82F6),
        onPressed: () {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => ChatScreen()),
          );
        },
        child: Icon(Icons.smart_toy_outlined, size: 40, color: Colors.black),
      ),
    );
  }
}
