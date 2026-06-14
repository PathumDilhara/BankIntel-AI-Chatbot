import 'package:chatbot_app/core/widgts/custom_button.dart';
import 'package:chatbot_app/features/chat/animations/typing_dot_animation.dart';
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
  final ValueNotifier<bool> isAnswerGenerating = ValueNotifier(false);

  void sendMessage() async {
    try {
      final model = MessageModel(role: "user", msg: controller.text);

      conversation.value = [...conversation.value, model];
      String msg = controller.text;
      controller.clear();
      isAnswerGenerating.value = true;

      addTypingMessage();
      await Future.delayed(Duration(seconds: 3));

      BotResponse botResponse = await APIHandlingService().chat(msg);
      print(botResponse);

      isAnswerGenerating.value = false;
      handleBotResponse(botResponse);
    } catch (err) {
      conversation.value =
          List.from(conversation.value)
            ..removeWhere((m) => m.isTyping == true)
            ..add(
              MessageModel(role: "bot", msg: "Error occurred", isError: true),
            );
    }
  }

  void addTypingMessage() {
    conversation.value = [
      ...conversation.value,
      MessageModel(role: "bot", msg: "", isTyping: true),
    ];
  }

  void handleBotResponse(BotResponse response) {
    conversation.value =
        List.from(conversation.value)
          ..removeWhere((m) => m.isTyping == true)
          ..add(
            MessageModel(
              role: "bot",
              msg: response.message,
              botResponse: response,
            ),
          );
  }

  @override
  Widget build(BuildContext context) {
    TextStyle textStyle = TextStyle(
      fontSize: 16,
      fontWeight: FontWeight.w400,
      color: Colors.black,
    );

    return Scaffold(
      backgroundColor: Color(0xFFF9FAFB),
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
                          bool isError = conversation.isError;
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
                                gradient: LinearGradient(
                                  colors:
                                      isError
                                          ? [
                                            Color(0xFFF87171),
                                            Color(0xFFDC2626),
                                          ]
                                          : isUser
                                          ? [
                                            Color(0xFF4F8CFF),
                                            Color(0xFF2563EB),
                                          ]
                                          : [
                                            Color(0xFFB6B9BF),
                                            Color(0xFF7E838A),
                                          ],
                                  begin: Alignment.topLeft,
                                  end: Alignment.bottomRight,
                                ),
                                borderRadius: BorderRadius.circular(15),
                              ),
                              child:
                                  isUser
                                      ? Text(
                                        conversation.msg!,
                                        softWrap: true,
                                        style: textStyle,
                                      )
                                      : Column(
                                        crossAxisAlignment:
                                            CrossAxisAlignment.start,
                                        children: <Widget>[
                                          if (conversation.msg == null ||
                                              conversation.msg!.isEmpty)
                                            Row(
                                              mainAxisSize: MainAxisSize.min,
                                              children: [
                                                Text(
                                                  "Thinking",
                                                  softWrap: true,
                                                  style: textStyle,
                                                ),
                                                SizedBox(width: 20,child: TypingDots()),
                                              ],
                                            )
                                          else
                                            Text(
                                              conversation.msg!,
                                              softWrap: true,
                                              style: textStyle,
                                            ),

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
                                                                top: 5,
                                                                bottom: 5.0,
                                                              ),
                                                          child: customButton(
                                                            title: e.label,
                                                            bgColor: Color(
                                                              0xFFBFDBFE,
                                                            ),
                                                            textColor:
                                                                Colors.black,
                                                            fontSize: 16,
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
