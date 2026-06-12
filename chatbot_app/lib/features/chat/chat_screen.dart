import 'package:chatbot_app/core/widgts/custom_button.dart';
import 'package:chatbot_app/features/chat/models/msg_model.dart';
import 'package:chatbot_app/features/chat/services/api_handeling_service.dart';
import 'package:flutter/material.dart';

import 'models/bot_response.dart';

class ChatScreen extends StatefulWidget {
  const ChatScreen({super.key});

  @override
  State<ChatScreen> createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  final TextEditingController controller = TextEditingController();

  final ValueNotifier<List<MessageModel>> conversation = ValueNotifier([]);

  void sendMessage() async {
    final model = MessageModel(role: "user", msg: controller.text);

    conversation.value = [...conversation.value, model];
    String msg = controller.text;
    controller.clear();
    BotResponse botResponse = await APIHandlingService().chat(msg);
    print(botResponse);
    handleBotResponse(botResponse);
  }

  void handleBotResponse(BotResponse response) {
    conversation.value = [
      ...conversation.value,
      MessageModel(role: "bot", msg: response.message, botResponse: response),
    ];
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          "AI Assistant",
          style: TextStyle(fontWeight: FontWeight.bold),
        ),
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Expanded(
              child: ValueListenableBuilder(
                valueListenable: conversation,
                builder: (context, value, child) {
                  bool isInitial = value.isEmpty;

                  return isInitial
                      ? Center(
                        child: Column(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Icon(
                              Icons.smart_toy_outlined,
                              size: 100,
                              color: Colors.blue,
                            ),
                            Text(
                              "Welcome to BankIntel AI",
                              style: TextStyle(
                                fontSize: 25,
                                fontWeight: FontWeight.bold,
                              ),
                            ),

                            const SizedBox(height: 10),

                            Text(
                              "Ask me anything about your banking services.",
                              textAlign: TextAlign.center,
                              style: TextStyle(
                                color: Colors.grey.shade600,
                                fontSize: 16,
                              ),
                            ),
                          ],
                        ),
                      )
                      : ListView.builder(
                        itemCount: value.length,
                        itemBuilder: (context, index) {
                          final conversation = value[index];
                          print("######### ${conversation.msg}");
                          bool isUser = conversation.role == "user";
                          bool hasOptions = false;

                          if (conversation.botResponse != null) {
                            hasOptions =
                                conversation.botResponse!.options.isNotEmpty;
                          }

                          return Align(
                            alignment:
                                isUser
                                    ? Alignment.centerRight
                                    : Alignment.centerLeft,
                            child: Container(
                              margin: EdgeInsets.symmetric(vertical: 4),
                              padding: EdgeInsets.all(12),
                              constraints: BoxConstraints(maxWidth: 250),
                              decoration: BoxDecoration(
                                color:
                                    isUser ? Colors.blue : Colors.grey.shade300,
                                borderRadius: BorderRadius.circular(12),
                              ),
                              child:
                                  isUser
                                      ? Text(
                                        conversation.msg!,
                                        style: TextStyle(
                                          color:
                                              isUser
                                                  ? Colors.white
                                                  : Colors.black,
                                        ),
                                      )
                                      : Column(
                                        crossAxisAlignment:
                                            CrossAxisAlignment.start,
                                        children: [
                                          Text(conversation.msg!),
                                          SizedBox(height: 10),

                                          if (hasOptions)
                                            Column(
                                              mainAxisSize: MainAxisSize.min,
                                              crossAxisAlignment:
                                                  CrossAxisAlignment.start,
                                              children:
                                                  conversation
                                                      .botResponse!
                                                      .options
                                                      .map((e) {
                                                        return Padding(
                                                          padding:
                                                              const EdgeInsets.only(
                                                                bottom: 5.0,
                                                              ),
                                                          child: customButton(
                                                            title: e.label,
                                                            bgColor: Colors.greenAccent
                                                                .withValues(
                                                                  alpha: 0.3,
                                                                ),
                                                            textColor:
                                                                Colors.black,
                                                            fontSize: 16
                                                          ),
                                                        );
                                                      })
                                                      .toList(),
                                            ),
                                        ],
                                      ),
                            ),
                          );
                        },
                      );
                },
              ),
            ),
            Container(
              padding: EdgeInsets.all(10),
              child: Row(
                children: [
                  Expanded(
                    child: TextField(
                      controller: controller,
                      decoration: InputDecoration(
                        hintText: "Type a message...",
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(100),
                        ),
                      ),
                    ),
                  ),
                  SizedBox(width: 10),
                  IconButton(
                    onPressed: () {
                      sendMessage();
                    },
                    icon: Icon(Icons.send, color: Colors.blue),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
