import { StyleSheet } from 'react-native';

export const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    justifyContent: 'center',  // Center content vertically when no categories
    alignItems: 'center',      // Center content horizontally when no categories
  },
  categoryButton: {
    backgroundColor: 'red',   // Red color for the category buttons
    width: 100,               // Fixed width to make the button square
    height: 100,              // Same height to ensure it's square
    justifyContent: 'center', // Center the text inside the button
    alignItems: 'center',
    margin: 10,               // Spacing between buttons
    borderRadius: 10,         // Rounded corners for the buttons
  },
  addButton: {
    backgroundColor: '#28a745',  // Green color for the + button
    width: 100,
    height: 100,
    justifyContent: 'center',
    alignItems: 'center',
    margin: 10,
    borderRadius: 10,
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold',
  },
  input: {
    borderWidth: 1,
    borderColor: '#ddd',
    padding: 10,
    borderRadius: 5,
    marginBottom: 10,
    width: '80%',
  },
  modalView: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'rgba(0,0,0,0.5)',  // Dimmed background for the modal
  },
  columnWrapper: {
    justifyContent: 'space-between',  // Align items in a row
  },
  // Style for the centered + button when there are no categories
  centeredAddButton: {
    backgroundColor: '#28a745',  // Green color for the + button
    width: 100,
    height: 100,
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 10,
  },
});