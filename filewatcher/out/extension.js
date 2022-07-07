"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const vscode = require("vscode");
// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
function activate(context) {
    const watcher = vscode.workspace.createFileSystemWatcher("**/*.{json}", false, false, false);
    watcher.onDidChange((uri) => {
        // IMPORTANT: Compile typescript file to javascript with STRG+SHIFT+B
        console.log("File changed : " + uri.fsPath);
        //Disable caching, else the change will not appear in output
        delete require.cache[uri.fsPath];
        var json = require(uri.fsPath);
        // var json1 = JSON.parse(json);
        // var text =JSON.stringify(json);
        console.log(json);
        // const rootNode = parseTree(text);
        // if(rootNode !== undefined ){
        // 	// Find first element of the "components" array
        // 	const firstComponent = findNodeAtLocation(rootNode, ["API"]);
        // 	if(firstComponent !== undefined ){
        // 		console.log(firstComponent);
        // 		if(json1 !== undefined ){
        // 			console.log(firstComponent.offset);
        // 			const start = json1.positionAt(firstComponent.offset);
        // 			const end = json1.positionAt(firstComponent.offset+ firstComponent.length);
        // 			console.log("TEST1");
        // 			const range = new vscode.Range(start, end);
        // 			console.log(range);
        // 			let diagnosticCollection = vscode.languages.createDiagnosticCollection("TEST");
        // 			let diagnostics : vscode.Diagnostic[] = [];
        // 			diagnostics.push(new vscode.Diagnostic(range, "test", vscode.DiagnosticSeverity.Warning));
        // 			// Ctrl+Shift+B To compile
        // 			console.log(diagnostics);
        // 			diagnosticCollection.set(uri, diagnostics);
        // 			console.log("TEST");
        // 		}
        // 	}
        // }
    });
}
exports.activate = activate;
// this method is called when your extension is deactivated
function deactivate() { }
exports.deactivate = deactivate;
